from constants import field
import readProcessMemory

class Players:
    def __init__(self):
        self.id = readProcessMemory.Read_MEM().player_pointers()[0]
        self.name = readProcessMemory.Read_MEM().player_pointers()[1]
        self.hp = 0
        self.lvl = 0
        self.augment = []

    def board(self):
        print(self.name)
        for k, v in field.items():
            if k == self.id:
                print(v)


if __name__ == "__main__":

    Players().player()
