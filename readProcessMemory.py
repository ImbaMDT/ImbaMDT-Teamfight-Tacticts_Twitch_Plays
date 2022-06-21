from pymem import Pymem
from pymem.exception import MemoryReadError

import constants

# reads the players and units coords

# TODO: get player coords
#       add the players into the constants.Field dict ? or add it into the json file.
#       get gold, shops, items, stage, exp left to level, get stage state (for example: can you drag and drop units?)

def champ_pointers():
    # Given constants.Process_Name
    # returns Object Name and Pos
    mem = Pymem(constants.PROCESS_NAME)
    field_offset = mem.read_int(mem.base_address + constants.oTFTObject)
    field_entity_object = mem.read_uint(field_offset + 0x04)

    for x in range(256):  # max loops
        field_iter = mem.read_uint(field_entity_object + (0x04 * x))
        try:
            field_object_bytes = mem.read_bytes(field_iter + 0x58, 0x4)
            if field_object_bytes == b'Obje':  # mem.read_uint == 1701470799

                champ_name_offset = mem.read_uint(field_iter + constants.oName)
                champ_name = mem.read_string(champ_name_offset + 0xE)  # + 0xE to delete the UID from the Units
                champ_x = round(mem.read_float(field_iter + constants.oX) + mem.read_float(field_iter + constants.oX2))
                champ_y = round(mem.read_float(field_iter + constants.oY) + mem.read_float(field_iter + constants.oY2))
                champ_coord = (champ_x, champ_y)

                if champ_coord in constants.field:
                    champ_name = champ_name.split('_')  # Delete the RoundCounter of an Unit / or .partition
                    constants.field[champ_coord] = champ_name[0]
                    print(constants.field)


        #                if TFTChampX > 12000 and TFTChampX < 17000 and TFTChampY > 21000 and TFTChampY < 27000:
        #            elif field_object_bytes == b'Cube':  # mem.read_uint == 1700951363
        #                print(FieldObjectInt)
        #                print(field_object_bytes)
        #                pass
        except MemoryReadError:
            break
    return champ_x, champ_y, champ_name[0]


def player_pointers():
    # Given constants.Process_Name
    # returns Name and Pos of the players
    mem = Pymem(constants.PROCESS_NAME)
    player_offsets = []
    player_offset = mem.read_int(mem.base_address + constants.oTFTChamps)
    player_offset2 = mem.read_int(player_offset + 0x04)

    for x in range(9):  # max loops
        field_iter = mem.read_uint(player_offset2 + (0x04 * x))
        try:
            field_object_bytes = mem.read_bytes(field_iter + 0x58, 0x4)
            if field_object_bytes == b'Obje':  # player_name is too large and a pointer now
                player_name_offset = mem.read_uint(field_iter + constants.oName)
                player_name = mem.read_string(player_name_offset)
                player_id = str(player_x + player_y)
                player_offsets.extend((player_id, player_name))
            else:
                player_name = mem.read_string(field_iter + constants.oName)
                player_x = round(mem.read_float(field_iter + constants.oX) + mem.read_float(field_iter + constants.oX2))
                player_y = round(mem.read_float(field_iter + constants.oY) + mem.read_float(field_iter + constants.oY2))
                player_id = str(player_x + player_y)
                player_offsets.extend((player_id, player_name))

        except MemoryReadError:
            break

    return player_offsets


if __name__ == "__main__":
    mem = Pymem(constants.PROCESS_NAME)

    player_pointers()