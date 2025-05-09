"""Generate hyper triggers to vastly improve trigger cycle speed."""
from richchk.model.richchk.trig.actions.preserve_trigger_action import PreserveTrigger
from richchk.model.richchk.trig.actions.wait_trigger_action import WaitAction
from richchk.model.richchk.trig.conditions.always_condition import AlwaysCondition
from richchk.model.richchk.trig.rich_trigger import RichTrigger

from ...data.players import PLAYER_OWNING_SYSTEMS
from ...model.map_build_context import MapBuildContext
from ...systems.trigger_generator import TriggerGenerator

_NUM_HYPER_TRIGGERS = 4
_NUM_WAITS = 63


def _create_single_hyper_trigger(map_build_context: MapBuildContext) -> list[RichTrigger]:
    triggers = []
    triggers.append(RichTrigger(_conditions=[AlwaysCondition()],
                               _actions=[WaitAction(_milliseconds=0) for _ in range(0, _NUM_WAITS)] + [PreserveTrigger()],
                               _players={PLAYER_OWNING_SYSTEMS}))
    return triggers


class HyperTriggersGenerator(TriggerGenerator):
    def generate_triggers(
        self, map_build_context: MapBuildContext
    ) -> list[RichTrigger]:
        triggers = []
        for _ in range(0, _NUM_HYPER_TRIGGERS):
            triggers += _create_single_hyper_trigger(map_build_context)
        return triggers
