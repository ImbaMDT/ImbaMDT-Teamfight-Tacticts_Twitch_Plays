from pymem import Pymem
from pymem.exception import MemoryReadError

import constants

# reads the players and units coords

# TODO: get player coords
#       add the players into the constants.Field dict ? or add it into the json file.
#       get gold, shops, items, stage, exp left to level, get stage state (for example: can you drag and drop units?)
#       check if you are able to read playernames

class Read_MEM:

    """ reads the game memory """
    in_game = False
    while not in_game:
        try:
            # get mem
            mem = Pymem(constants.PROCESS_NAME)
            mem.read_int(mem.base_address)
            in_game = True
        except:
            pass
    # other code that uses result but is not involved in getting it
#    mem = Pymem(constants.PROCESS_NAME)

    """ getting the playernames and playercoords """
    def player_pointers(self):
        # given constants.Process_Name
        # returns Name and Pos of the players
        player_offsets = []
        player_offset = self.mem.read_int(self.mem.base_address + constants.oTFTChamps)
        player_offset2 = self.mem.read_int(player_offset + 0x04)

        for x in range(8):  # max loops
            field_iter = self.mem.read_uint(player_offset2 + (0x04 * x))
            try:
                field_object_bytes = self.mem.read_bytes(field_iter + 0x58, 0x4)
                if field_object_bytes == b'Obje':  # player_name is too large and a pointer now
                    player_name_offset = self.mem.read_uint(field_iter + constants.oName)
                    player_name = self.mem.read_string(player_name_offset)
                    player_id = str(player_x + player_y)
                    player_offsets.extend((player_id, player_name))
                else:
                    player_name = self.mem.read_string(field_iter + constants.oName)
                    player_x = round(self.mem.read_float(field_iter + constants.oX) + self.mem.read_float(field_iter + constants.oX2))
                    player_y = round(self.mem.read_float(field_iter + constants.oY) + self.mem.read_float(field_iter + constants.oY2))
                    player_id = str(player_x + player_y)
                    player_offsets.extend((player_id, player_name))

                print(player_offsets)
            except MemoryReadError:
                break

        return player_offsets

    """ getting every champ existing atm """
    def champ_pointers(self):
        # given constants.Process_Name
        # returns Object Name and Pos
        field_offset = self.mem.read_int(self.mem.base_address + constants.oTFTObject)
        field_entity_object = self.mem.read_uint(field_offset + 0x04)

        for x in range(256):  # max loops
            field_iter = self.mem.read_uint(field_entity_object + (0x04 * x))
            try:
                field_object_bytes = self.mem.read_bytes(field_iter + 0x58, 0x4)
                if field_object_bytes == b'Obje':  # mem.read_uint == 1701470799

                    champ_name_offset = self.mem.read_uint(field_iter + constants.oName)
                    champ_name = self.mem.read_string(champ_name_offset + 0xE)  # + 0xE to delete the UID from the Units
                    champ_x = round(self.mem.read_float(field_iter + constants.oX) + self.mem.read_float(field_iter + constants.oX2))
                    champ_y = round(self.mem.read_float(field_iter + constants.oY) + self.mem.read_float(field_iter + constants.oY2))
                    champ_coord = (champ_x, champ_y)
                    print(champ_name)

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


if __name__ == "__main__":

    p = Read_MEM()
    p.champ_pointers()