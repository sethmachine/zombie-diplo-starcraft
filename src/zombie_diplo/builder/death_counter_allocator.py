"""Allocates undefined DeathCounter objects defined Player and Unit ID values."""
from typing import Generator

from richchk.model.richchk.trig.player_id import PlayerId
from richchk.model.richchk.unis.unit_id import UnitId

from ..builder.possible_death_counters import (
    generate_possible_death_counter_units,
    generate_possible_death_counters,
)
from ..model.allocated_death_counter import AllocatedDeathCounter
from ..model.death_counter import DeathCounter
from ..util.logger import get_logger


class DeathCounterAllocator:
    def __init__(self) -> None:
        self._log = get_logger(DeathCounterAllocator.__name__)
        self._allocated_dcs: dict[DeathCounter, AllocatedDeathCounter] = {}
        self._possible_dcs = generate_possible_death_counters()
        self._used_allocated_dcs: set[AllocatedDeathCounter] = set()
        self._possible_units_for_player: dict[
            PlayerId, Generator[UnitId, None, None]
        ] = {player: generate_possible_death_counter_units() for player in PlayerId}

    def get_or_allocate(self, dc: DeathCounter) -> AllocatedDeathCounter:
        if dc not in self._allocated_dcs:
            if dc.player and dc.unit:
                ac = AllocatedDeathCounter(_player=dc.player, _unit=dc.unit)
                self._allocated_dcs[dc] = ac
                self._used_allocated_dcs.add(ac)
                return ac
            if not dc.player and not dc.unit:
                ac = next(self._possible_dcs)
                self._allocated_dcs[dc] = ac
                self._used_allocated_dcs.add(ac)
                return ac
            elif dc.player and not dc.unit:
                for unit in self._possible_units_for_player[dc.player]:
                    maybe_ac = AllocatedDeathCounter(_player=dc.player, _unit=unit)
                    if maybe_ac not in self._used_allocated_dcs:
                        self._allocated_dcs[dc] = maybe_ac
                        self._used_allocated_dcs.add(maybe_ac)
                        return maybe_ac
                msg = f"Exhausted death counters for player: {dc.player}"
                self._log.error(msg)
                raise ValueError(msg)
            else:
                msg = f"Death counters cannot have an undefined player and a defined unit!: {dc}"
                self._log.error(msg)
                raise ValueError(msg)
        else:
            return self._allocated_dcs[dc]
