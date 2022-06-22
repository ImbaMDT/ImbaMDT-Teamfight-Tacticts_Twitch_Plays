import json
from readProcessMemory import Read_MEM

# writes and reads from a json file

# TODO: rework the iterations
#

class Read_Json:

    """ passing variables from "readProcessMemory" to the Json file "game_infos" """
    with open('game_infos.json') as f:
        data = json.load(f)

    def write_json(self):
        with open('game_infos.json', 'w') as f:
            json.dump(self.data, f, indent=4, sort_keys=True)

    """ passing the playernames """
    def player_names(self):                # changes playernames
        player_id = Read_MEM().player_pointers()
        x = 0
        y = 1
        for i in range(8):
            for item in self.data['players']['%s' %player_id[x]]:
                item['playername'] = '%s' %player_id[y]
                print(item['playername'])
                Read_Json.write_json(self.data)
            x += 2
            y += 2

    """ passing the championnames and coords """
    def champion_names(self):
        champ_id = Read_MEM.champ_pointers()
        x = 0
        y = 1
        z = 2
        for i in range(128):                    # find a better way to iterate through an expending list
            for item in self.data['champs']['%s' %champ_id[x]]['%s' %champ_id[y]]:
                item['champname'] = '%s' % champ_id[z]
                print(item['playername'])
            x += 3
            y += 3
            z += 3

def test():
    with open('game_infos.json') as f:
        data = json.load(f)
    champ_id = '13284'
    champ_id2 = '26396'
    for item in data['champs']['%s' %champ_id]['%s' %champ_id2]:
        print(item['champname'])





if __name__ == "__main__":
    Read_Json().player_names()

#    with open('set_updates.json', 'w') as f:
#        json.dump(data, f, indent=4, sort_keys=True)