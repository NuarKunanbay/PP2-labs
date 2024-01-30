import json
print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
with open('sample-data.json', 'r') as file:
        f = json.load(file)
        for el in f['imdata']:
                print(el["l1PhysIf"]['attributes']['dn'], '                             ', el["l1PhysIf"]['attributes']['dn'], '', el["l1PhysIf"]['attributes']['dn'])