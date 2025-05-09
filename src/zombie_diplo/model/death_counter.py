"""Represent an unallocated death counter for triggers.

Death counters are used to store arbitrary integer values and are a unique combination
of a PlayerId and a UnitId value.  These are used for SetDeathsAction and
DeathsCondition.

Both values are optional.  If at least one is not filled in, an appropriate value will
be filled in.  If both values are filled in, they will be respected.
"""
import dataclasses
from typing import Optional

from richchk.model.richchk.trig.player_id import PlayerId
from richchk.model.richchk.unis.unit_id import UnitId


@dataclasses.dataclass(frozen=True)
class DeathCounter:
    _player: Optional[PlayerId] = None
    _unit: Optional[UnitId] = None

    @property
    def player(self) -> Optional[PlayerId]:
        return self._player

    @property
    def unit(self) -> Optional[UnitId]:
        return self._unit

    def __eq__(self, other: object) -> bool:
        if isinstance(other, DeathCounter):
            if any(
                [
                    self.unit is None,
                    self.player is None,
                    other.unit is None,
                    other.player is None,
                ]
            ):
                return id(self) == id(other)
            else:
                return all([self.unit == other.unit, self.player == other.player])
        return False

    def __hash__(self) -> int:
        if any([not self.player, not self.unit]):
            return hash(id(self))
        return hash((self.player, self.unit))
