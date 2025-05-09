"""Builds Zombie Diplo map.
"""
import os
import time

from richchk.editor.richchk.rich_chk_editor import RichChkEditor
from richchk.editor.richchk.rich_trig_editor import RichTrigEditor
from richchk.io.mpq.starcraft_mpq_io_helper import StarCraftMpqIoHelper
from richchk.io.richchk.query.chk_query_util import ChkQueryUtil
from richchk.model.richchk.trig.rich_trig_section import RichTrigSection
from richchk.model.richchk.trig.rich_trigger import RichTrigger

from zombie_diplo.builder.death_counter_allocator import DeathCounterAllocator
from zombie_diplo.builder.location_reference_resolver import (
    LocationReferenceResolver,
)
from zombie_diplo.builder.wav_file_resolver import WavFileResolver
from zombie_diplo.model.map_build_context import MapBuildContext
from zombie_diplo.systems.hypertriggers.hyper_triggers_generator import HyperTriggersGenerator

MAPS_DIR = "data/maps"

# map file with terrain and locations only
MAPFILE = os.path.join(MAPS_DIR, "zombie-diplo-terrain.scx")
# output map file that will contain terrain, triggers, unit settings, etc.
OUTFILE = os.path.join(MAPS_DIR, "zombie-diplo-playable.scx")


def _generate_all_triggers(context: MapBuildContext) -> list[RichTrigger]:
    trigs = HyperTriggersGenerator().generate_triggers(map_build_context=context)
    return trigs


def _build_map(path_to_base_mpq_file: str, path_to_new_mpq_file: str):
    mpqio = StarCraftMpqIoHelper.create_mpq_io()
    chk = mpqio.read_chk_from_mpq(path_to_base_mpq_file)
    loc_resolver = LocationReferenceResolver(chk=chk)
    dca = DeathCounterAllocator()
    context = MapBuildContext(
        _chk=chk,
        _death_counter_allocator=dca,
        _location_reference_resolver=loc_resolver,
        _wavfile_resolver=WavFileResolver(chk=chk, wavfile_mapping={}),
    )
    trigs = _generate_all_triggers(context)
    chkeditor = RichChkEditor()
    new_trig = RichTrigEditor.add_triggers(
        trigs, ChkQueryUtil.find_only_rich_section_in_chk(RichTrigSection, chk)
    )
    new_chk = chkeditor.replace_chk_section(new_trig, chk)
    mpqio.save_chk_to_mpq(
        new_chk,
        path_to_base_mpq_file,
        path_to_new_mpq_file,
        overwrite_existing=True,
    )
    print(f"Total map triggers: {len(new_trig.triggers)}")


if __name__ == "__main__":
    start_time = time.time()

    _build_map(MAPFILE, OUTFILE)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Built map in {elapsed_time:.4f} seconds.")
