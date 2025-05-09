from richchk.model.richchk.unis.unit_id import UnitId

from zombie_diplo.model.colony.zombie_evolution import ZombieEvolution

BASE_ZOMBIE_BUILDING = UnitId.ZERG_NYDUS_CANAL

ZOMBIE_EVOLUTIONS = [ZombieEvolution(_from_unit=BASE_ZOMBIE_BUILDING, _to_unit=UnitId.ZERG_CREEP_COLONY),
                     ZombieEvolution(_from_unit=UnitId.ZERG_SPORE_COLONY, _to_unit=UnitId.ZERG_SPIRE),
                     ZombieEvolution(_from_unit=UnitId.ZERG_GREATER_SPIRE, _to_unit=UnitId.INFESTED_TERRAN)]