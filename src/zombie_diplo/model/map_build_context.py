"""Represent all the context needed to update a RichChk when building a map."""
import dataclasses

from richchk.model.richchk.mrgn.rich_location import RichLocation
from richchk.model.richchk.rich_chk import RichChk

from ..builder.death_counter_allocator import DeathCounterAllocator
from ..builder.location_reference_resolver import LocationReferenceResolver
from ..builder.wav_file_resolver import WavFileResolver
from .location_reference import LocationReference


@dataclasses.dataclass
class MapBuildContext:
    _chk: RichChk
    _death_counter_allocator: DeathCounterAllocator
    _location_reference_resolver: LocationReferenceResolver
    _wavfile_resolver: WavFileResolver

    def __post_init__(self) -> None:
        self._anywhere_location = self._location_reference_resolver.resolve_exactly(
            LocationReference(_name="anywhere")
        )

    @property
    def chk(self) -> RichChk:
        return self._chk

    @property
    def death_counter_allocator(self) -> DeathCounterAllocator:
        return self._death_counter_allocator

    @property
    def location_reference_resolver(self) -> LocationReferenceResolver:
        return self._location_reference_resolver

    @property
    def wavfile_resolver(self) -> WavFileResolver:
        return self._wavfile_resolver

    @property
    def anywhere_location(self) -> RichLocation:
        return self._anywhere_location
