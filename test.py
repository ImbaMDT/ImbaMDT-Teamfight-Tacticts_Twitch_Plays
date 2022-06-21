from constants import field

# file to test stuff


translate = {}
new_dict = {}
for k, v in field.items():
    print("This is the key: '%s' and this is the value '%s'\n" % (k, v) )
    new_key = input("Please enter a new key: ")
    translate[k] = new_key

for old, new in translate.items():
    field[new] = field.pop(old)

print(field)