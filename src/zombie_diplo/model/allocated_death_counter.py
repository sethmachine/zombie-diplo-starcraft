"""Represent an allocated death counter for triggers.

Death counters are used to store arbitrary integer values and are a unique combination
of a PlayerId and a UnitId value.  These are used for SetDeathsAction and
DeathsCondition.
"""
import dataclasses

from richchk.model.richchk.trig.player_id import PlayerId
from richchk.model.richchk.unis.unit_id import UnitId


@dataclasses.dataclass(frozen=True)
class AllocatedDeathCounter:
    _player: PlayerId
    _unit: UnitId

    @property
    def player(self) -> PlayerId:
        return self._player

    @property
    def unit(self) -> UnitId:
        return self._unit
