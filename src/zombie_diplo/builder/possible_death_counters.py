"""Defines all possible/safe to use death counters.


Update this list as needed depending on your map and what units are never used or can never be killed.
"""
import itertools
from typing import Generator

from richchk.model.richchk.trig.player_id import PlayerId
from richchk.model.richchk.unis.unit_id import UnitId

from ..model.allocated_death_counter import AllocatedDeathCounter

# these are computer players that always exist until the game is over
_ALWAYS_PRESENT_PLAYERS = [PlayerId.PLAYER_8]
# these units cannot normally be killed or spawned under typical circumstances
# you can also add any other units you want,
# as long as you guarantee the above players can't ever have deaths of them
_SAFE_UNITS = [
    UnitId.ALAN_SCHEZAR_TURRET,  # 'Alan Turret'
    UnitId.CANTINA,  # 'Cantina'
    UnitId.CAVE,  # 'Cave'
    UnitId.CAVEIN,  # 'Cave-in'
    UnitId.DISRUPTION_WEB,  # 'Disruption Field'
    UnitId.EDMUND_DUKE_TURRET,  # 'Duke Turret type 1'
    UnitId.EDMUND_DUKE_TURRET_SIEGE_MODE,  # 'Duke Turret type 2'
    UnitId.GOLIATH_TURRET,  # 'Goliath Turret'
    UnitId.INDEPENDANT_COMMAND_CENTER,  # 'Independent Command Center'
    UnitId.INDEPENDANT_STARPORT,  # 'Independent Starport'
    UnitId.INDEPENDANT_JUMP_GATE,  # 'Jump Gate'
    UnitId.KHAYDARIN_CRYSTAL_FORMATION,  # 'Khaydarin Crystal Formation'
    UnitId.KYADARIN_CRYSTAL_FORMATION,  # 'Kyadarin Crystal Formation'
    UnitId.MINING_PLATFORM,  # 'Mining Platform'
    UnitId.NUCLEAR_MISSILE,  # 'Nuclear Missile'
    UnitId.PROTOSS_MARKER,  # 'Protoss Marker'
    UnitId.UNUSED_PROTOSS_BUILDING_1,  # 'Protoss Unused type 1'
    UnitId.UNUSED_PROTOSS_BUILDING_2,  # 'Protoss Unused type 2'
    UnitId.PSI_EMITTER,  # 'Psi Emitter'
    UnitId.RIGHT_PIT_DOOR,  # 'Right Pit Door'
    UnitId.RIGHT_UPPER_LEVEL_DOOR,  # 'Right Upper Level Door'
    UnitId.RIGHT_WALL_FLAME_TRAP,  # 'Right Wall Flame Trap'
    UnitId.RIGHT_WALL_MISSILE_TRAP,  # 'Right Wall Missile Trap'
    UnitId.RUINS,  # 'Ruins'
    UnitId.SCANNER_SWEEP,  # 'Scanner Sweep'
    UnitId.START_LOCATION,  # 'Start Location'
    UnitId.TANK_TURRET_TANK_MODE,  # 'Tank Turret type 1'
    UnitId.TANK_TURRET_SIEGE_MODE,  # 'Tank Turret type 2'
    UnitId.TERRAN_BEACON,  # 'Terran Beacon'
    UnitId.PROTOSS_BEACON,  # 'Protoss Beacon'
    UnitId.TERRAN_FLAG_BEACON,  # 'Terran Flag Beacon'
    UnitId.PROTOSS_FLAG_BEACON,  # 'Protoss Flag Beacon'
    UnitId.TERRAN_MARKER,  # 'Terran Marker'
    UnitId.PROTOSS_OBSERVATORY,  # 'Protoss Observatory'
    UnitId.UNUSED_WAS_STARBASE,  # 'Unused type 1'
    UnitId.UNUSED_WAS_CARGO_SHIP,  # 'Unused type 2'
    UnitId.UNUSED_WAS_MERCENARY_GUNSHIP,  # 'Unused Terran Bldg type 1'
    UnitId.UNUSED_WAS_REPAIR_BAY,  # 'Unused Terran Bldg type 2'
    UnitId.UNUSED_ZERG_BUILDING,  # 'Unused Zerg Bldg'
    UnitId.UNUSED_ZERG_BUILDING_5,  # 'Unused Zerg Bldg 5'
    UnitId.VESPENE_GEYSER,  # 'Vespene Geyser'
    UnitId.ZERG_BEACON,  # 'Zerg Beacon'
    UnitId.ZERG_FLAG_BEACON,  # 'Zerg Flag Beacon'
    UnitId.DARK_SWARM,  # 'Dark Swarm'
    UnitId.DATA_DISC,  # 'Data Disc'
    UnitId.MUTALISK_GUARDIAN_COCOON,  # 'Cocoon'
    UnitId.ZERG_EGG,  # 'Zerg Egg'
    UnitId.FLAG,  # 'Flag'
    UnitId.FLOOR_GUN_TRAP,  # 'Floor Gun Trap'
    UnitId.FLOOR_HATCH,  # 'Floor Hatch (UNUSED)'
    UnitId.FLOOR_MISSILE_TRAP,  # 'Floor Missile Trap'
    UnitId.LEFT_PIT_DOOR,  # 'Left Pit Door'
    UnitId.LEFT_UPPER_LEVEL_DOOR,  # 'Left Upper Level Door'
    UnitId.LEFT_WALL_FLAME_TRAP,  # 'Left Wall Flame Trap'
    UnitId.LEFT_WALL_MISSILE_TRAP,  # 'Left Wall Missile Trap'
    UnitId.MINERAL_FIELD_TYPE_1,  # 'Mineral Field (Type 1)'
    UnitId.MINERAL_FIELD_TYPE_2,  # 'Mineral Field (Type 2)'
    UnitId.MINERAL_FIELD_TYPE_3,  # 'Mineral Field (Type 3)'
    UnitId.PROTOSS_VESPENE_GAS_ORB_TYPE_1,  # 'Vespene Orb (Protoss Type 1)'
    UnitId.PROTOSS_VESPENE_GAS_ORB_TYPE_2,  # 'Vespene Orb (Protoss Type 2)'
    UnitId.ZERG_VESPENE_GAS_SAC_TYPE_1,  # 'Vespene Sac (Zerg Type 1)'
    UnitId.ZERG_VESPENE_GAS_SAC_TYPE_2,  # 'Vespene Sac (Zerg Type 2)'
    UnitId.TERRAN_VESPENE_GAS_TANK_TYPE_1,  # 'Vespene Tank (Terran Type 1)'
    UnitId.TERRAN_VESPENE_GAS_TANK_TYPE_2,  # 'Vespene Tank (Terran Type 2)'
    UnitId.URSADON_ICE_WORLD_CRITTER,  # 'Ursadon (Ice World)'
    UnitId.BENGALAAS_JUNGLE_CRITTER,  # 'Bengalaas (Jungle)'
    UnitId.RHYNADON_BADLANDS_CRITTER,
    UnitId.KAKARU_TWILIGHT_CRITTER,
    UnitId.SCANTID_DESERT_CRITTER,
    UnitId.RAGNASAUR_ASHWORLD_CRITTER,
    UnitId.URAJ_CRYSTAL,
    UnitId.KHALIS_CRYSTAL,
    UnitId.KHAYDARIN_CRYSTAL,
]


def generate_possible_death_counters() -> Generator[AllocatedDeathCounter, None, None]:
    for (player, unit) in itertools.product(_ALWAYS_PRESENT_PLAYERS, _SAFE_UNITS):
        yield AllocatedDeathCounter(_player=player, _unit=unit)


def generate_possible_death_counter_units() -> Generator[UnitId, None, None]:
    for unit in _SAFE_UNITS:
        yield unit
