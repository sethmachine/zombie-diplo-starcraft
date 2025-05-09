"""Transform between one unit to another
"""
import dataclasses
from typing import Optional

from richchk.model.richchk.trig.player_id import PlayerId
from richchk.model.richchk.unis.unit_id import UnitId


@dataclasses.dataclass(frozen=True)
class ZombieEvolution:
    _from_unit: UnitId
    _to_unit: UnitId

    @property
    def player(self) -> Optional[PlayerId]:
        return self._player

    @property
    def from_unit(self) -> UnitId:
        return self._from_unit

    @property
    def to_unit(self) -> UnitId:
        return self._to_unit
