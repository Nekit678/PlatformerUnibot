from typing import List
import os

from Level_Module.EffectsMap import DamageBlock, GravityBlock, KillBlock, SlowBlock, SpeedBlock, JumpBlock
from Level_Module.Level import Level
from Level_Module.PhysicsMap import CommonBlock
from Level_Module.Player import Player

types_id = {
    0: Level.set_player,
    1: Level.add_enemy,
    2: Level.add_bonus,
    3: Level.add_complete_block,
    4: Level.add_edge_block,
    5: Level.add_map_sprite_block,
    6: Level.add_physics_map_block,
    7: Level.add_physics_effect_map_block
}

items_id = {
    0: Player,
    1: GravityBlock,
    2: SpeedBlock,
    3: SlowBlock,
    4: KillBlock,
    5: DamageBlock,
    6: CommonBlock,
    7: JumpBlock
}


class Parser:
    @staticmethod
    def get_lvl_list():
        files = os.listdir('Levels')
        lvl_files: List[str] = []
        for file in files:
            if file.find(".pltlvl") != -1:
                lvl_files.append(file)
        return lvl_files

    @staticmethod
    def load_level(lvl_pathname: str):
        Level.clear_level()
        with open(f"Levels\{lvl_pathname}", "r") as lvl_file:
            for line in lvl_file:
                item = line.replace("\n", "")
                info = item.split(sep=" ")
                item_type = int(info[0])
                item_id = int(info[1])
                item_args = []
                for arg in info[2:]:
                    item_args.append(int(arg))
                print(item_type, item_id, item_args)
                types_id[item_type](items_id[item_id](*item_args))
