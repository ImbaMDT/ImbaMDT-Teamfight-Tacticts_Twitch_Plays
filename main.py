from pymem import Pymem

from constants import PROCESS_NAME
import readProcessMemory


# TODO: get player coords
#       add the players into the constants.Field dict
#       get gold, shops, items, stage, exp left to level, get stage state (for example: can you drag and drop units?)





if __name__ == "__main__":
    readProcessMemory.player_pointers(mem=Pymem(PROCESS_NAME))