"""Generates the triggers for a particular trigger system for the map's business
logic."""
from abc import abstractmethod

from richchk.model.richchk.trig.rich_trigger import RichTrigger

from ..model.map_build_context import MapBuildContext


class TriggerGenerator:
    @abstractmethod
    def generate_triggers(
        self, map_build_context: MapBuildContext
    ) -> list[RichTrigger]:
        raise NotImplementedError
