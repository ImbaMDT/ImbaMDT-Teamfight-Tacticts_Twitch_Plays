import json
import readProcessMemory

# writes and reads from an json file

def read_json():
    with open('game_infos.json') as f:
        data = json.load(f)

    return data

def write_json(data):
    with open('game_infos.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)

def player_names():                # changes playernames
    data = read_json()
    player_id = readProcessMemory.player_pointers()
    x = 0
    y = 1
    for i in range(8):
        for item in data['players']['%s' %player_id[x]]:
            item['playername'] = '%s' %player_id[y]
            print(item['playername'])
            write_json(data)
        x += 2
        y += 2

def champions():
    data = read_json()
    champ_id = readProcessMemory.champ_pointers()
    x = 0
    y = 1
    z = 2
    for i in range (128):
        for item in data['champs']['%s' %champ_id[x]]['%s' %champ_id[y]]:
            item['champname'] = '%s' % champ_id[z]
            print(item['playername'])
        x += 3
        y += 3
        z += 3

def test():
    data = read_json()
    champ_id = '13284'
    champ_id2 = '26396'
    for item in data['champs']['%s' %champ_id]['%s' %champ_id2]:
        print(item['champname'])





if __name__ == "__main__":

    champions()

#    with open('set_updates.json', 'w') as f:
#        json.dump(data, f, indent=4, sort_keys=True)