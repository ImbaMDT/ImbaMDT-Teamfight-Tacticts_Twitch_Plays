import json

# Not part of the actual program, crops the json you get from the ddragon api into something easier useable

# champion: name, cost, traits
# items: name, combined from

# if dragon = board size 2 else 1

# if id / from negative -> delete


def merge(a, b, path=None):
    "merges b into a"
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass # same leaf value
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a

def item_translate(data):
    # define desired replacements here
    translate_list = {"1": "BFSword", "2": "RecurveBow","3": "NeedlesslyLargeRod", "4": "TearoftheGoddess",
           "5": "ChainVest", "6": "NegatronCloak","7": "GiantsBelt", "8": "Spatula",
           "9": "SparringGloves"}

    x_list = []
    for item in data['items']:
        if item.get('from'):     #and x in item.get('from'):
            x_list.append(item.get('from'))

    flat_list = [item for sublist in x_list for item in sublist]
    print('Original list', x_list)
    print('Transformed list', flat_list)
    print(type(flat_list))
    stringlist = [str(x) for x in flat_list]
    datastring = []
    for string in stringlist:
        # use these three lines to do the replacement
        rep = dict((re.escape(k), v) for k, v in translate_list.iteritems())
        # Python 3 renamed dict.iteritems to dict.items so use rep.items() for latest versions
        pattern = re.compile("|".join(rep.keys()))
        text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    print(datastring)

def del_items(data):                # del useless stuff from items
    for item in data['items']:
        del item['desc']
        del item['effects']
        del item['icon']
        del item['id']
#        if not item.get('from'):       # del empty from
#            del item['from']

def del_champs(data):               # del useless stuff from champions and replace items for better storing
    for item in data['sets']['7']['champions']:
        del item['ability']
        del item['stats']
        del item['apiName']
        item['icon'] = item['icon'].replace("%(icon)s" % item, "%(name)s" % item)

def del_traits(data):
    for item in data['sets']['7']['traits']:
        del item['desc']
        del item['apiName']
        del item['icon']

        for x in item['effects']:
            del x['variables']

def player_names(data):                # changes playernames
    player_id = player_pointers()
    print(data['players']['29602']['3284'])
    data['players'].update(player_id)
#            x['playername'] = player_name[y]
#            print(x)
#            y += 1

def type_check(data):
    for item in data["players"]['29602']:
        print(type(item))



if __name__ == "__main__":
    with open('set_updates.json') as f:
        data = json.load(f)

    player_names(data)

#    with open('set_updates.json', 'w') as f:
#        json.dump(data, f, indent=4, sort_keys=True)