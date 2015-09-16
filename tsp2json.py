import pathlib
import json
import collections

for f in pathlib.Path('tsp').iterdir():
    if f.is_file() and str(f)[-3:] == 'tsp' :
        tsp = ''.join(open(str(f))).split('\n')
        j = collections.OrderedDict()
        for i in range(5):
            key, val = tsp[i].split(':')
            j[key.strip()] = val.strip()
        # - Dict
        j['NODE_COORD_SECTION'] = {}
        print(tsp[5])
        for coord in tsp[6:-2]:
            tmp = coord.strip().replace('  ',' ').replace('  ',' ')
            index, x, y = tmp.split(' ')
            j['NODE_COORD_SECTION'][index] = {'x': x, 'y': y}
        with open('dict/' + f.name + '.json', 'w') as f2:
            f2.write(json.dumps(j, indent=4))
        # - List
        j['NODE_COORD_SECTION'] = []
        for coord in tsp[6:-2]:
            coord = coord.strip().replace('  ',' ').replace('  ',' ')
            index, x, y = coord.split(' ')
            j['NODE_COORD_SECTION'].append({'x': x, 'y': y})
        with open('list/' + f.name + '.json', 'w') as f2:
            f2.write(json.dumps(j, indent=4))
        
