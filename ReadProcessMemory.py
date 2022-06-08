import constants
from pymem import Pymem
from pymem.exception import MemoryReadError


def field_pointers(mem):
    # Given constants.Process_Name
    # returns Object Name and Pos
    FieldOffset = mem.read_int(mem.base_address + constants.oTFTObject)
    FieldEntityObject = mem.read_uint(FieldOffset + 0x04)

    for x in range(256):  # max loops
        FieldIter = mem.read_uint(FieldEntityObject + (0x04 * x))
        try:
            FieldObjectBytes = mem.read_bytes(FieldIter + 0x58, 0x4)
            if FieldObjectBytes == b'Obje':  # mem.read_uint == 1701470799

                ChampNameOffset = mem.read_uint(FieldIter + constants.oName)
                ChampName = mem.read_string(ChampNameOffset + 0xE)  # + 0xE to delete the UID from the Units
                ChampX = round(mem.read_float(FieldIter + constants.oX) + mem.read_float(FieldIter + constants.oX2))
                ChampY = round(mem.read_float(FieldIter + constants.oY) + mem.read_float(FieldIter + constants.oY2))
                champcoord = (ChampX, ChampY)

                if champcoord in constants.Field:
                    ChampName = ChampName.split('_')  # Delete the RoundCounter of an Unit / or .partition
                    constants.Field[champcoord] = ChampName[0]


        #                if TFTChampX > 12000 and TFTChampX < 17000 and TFTChampY > 21000 and TFTChampY < 27000:
        #            elif FieldObjectBytes == b'Cube':  # mem.read_uint == 1700951363
        #                print(FieldObjectInt)
        #                print(FieldObjectBytes)
        #                pass
        except MemoryReadError:
            print(constants.Field)
            break
    return

def player_pointers(mem):
    # Given constants.Process_Name
    # returns Object Name and Pos
    PlayerOffset = mem.read_int(mem.base_address + constants.oTFTChamps)
    PlayerOffset2 = mem.read_int(PlayerOffset + 0x04)

    for x in range(8): # wann fängt es an?
        FieldIter = mem.read_uint(PlayerOffset2 + (0x04*x))
        try:
            playerName = mem.read_string(FieldIter + constants.oName)
            playerX = mem.read_float(FieldIter + constants.oX) + mem.read_float(FieldIter + constants.oX2)
            playerY = mem.read_float(FieldIter + constants.oY) + mem.read_float(FieldIter + constants.oY2)
        except ownName:
            ownName = mem.read_string(FieldIter + constants.oName)
            ownX = mem.read_float(FieldIter + constants.oX) + mem.read_float(FieldIter + constants.oX2)
            ownY = mem.read_float(FieldIter + constants.oY) + mem.read_float(FieldIter + constants.oY2)

            print(ownName)
    return



if __name__ == "__main__":
    mem = Pymem(constants.PROCESS_NAME)
    field_pointers(mem)