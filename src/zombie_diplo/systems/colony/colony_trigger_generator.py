"""Generate triggers for Creep Colony manipulation."""
from richchk.model.richchk.trig.actions.preserve_trigger_action import PreserveTrigger
from richchk.model.richchk.trig.actions.wait_trigger_action import WaitAction
from richchk.model.richchk.trig.conditions.always_condition import AlwaysCondition
from richchk.model.richchk.trig.conditions.command_condition import CommandCondition
from richchk.model.richchk.trig.conditions.comparators.numeric_comparator import NumericComparator
from richchk.model.richchk.trig.player_id import PlayerId
from richchk.model.richchk.trig.rich_trigger import RichTrigger

from .colony_data import BASE_ZOMBIE_BUILDING
from ...data.players import PLAYER_OWNING_SYSTEMS
from ...model.location_reference import LocationReference
from ...model.map_build_context import MapBuildContext
from ...systems.trigger_generator import TriggerGenerator

_NUM_HYPER_TRIGGERS = 4
_NUM_WAITS = 63

_NYDUS_AREA_LOC = LocationReference(_name="Nydus Area")
_BUILDING_REPLACEMENT_LOC = LocationReference(_name="Building Replacement")


def _center_on_nydus_canal(map_build_context: MapBuildContext) -> list[RichTrigger]:
    triggers = []
    triggers.append(RichTrigger(_conditions=[CommandCondition(_group=PlayerId.CURRENT_PLAYER,
                                              _comparator=NumericComparator.AT_LEAST,
                                              _amount=1, _unit=BASE_ZOMBIE_BUILDING)],
                               _actions=[WaitAction(_milliseconds=0) for _ in range(0, _NUM_WAITS)] + [PreserveTrigger()],
                               _players={PLAYER_OWNING_SYSTEMS}))
    return triggers

def _create_single_hyper_trigger(map_build_context: MapBuildContext) -> list[RichTrigger]:
    triggers = []
    triggers.append(RichTrigger(_conditions=[AlwaysCondition()],
                               _actions=[WaitAction(_milliseconds=0) for _ in range(0, _NUM_WAITS)] + [PreserveTrigger()],
                               _players={PLAYER_OWNING_SYSTEMS}))
    return triggers


class ColonyTriggerGenerator(TriggerGenerator):
    def generate_triggers(
        self, map_build_context: MapBuildContext
    ) -> list[RichTrigger]:
        triggers = []
        for _ in range(0, _NUM_HYPER_TRIGGERS):
            triggers += _create_single_hyper_trigger(map_build_context)
        return triggers
