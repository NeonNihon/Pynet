#!/usr/bin/env python
import yaml
import json


dr_seuss = "Box Fox House Mouse"
final_list = []

for word in dr_seuss.split():
    if word == 'House':
        final_list.append(word)
        final_list.append({})
        final_list[-1]['could_you'] = False
        final_list[-1]['would_you'] = False
    else:
        final_list.append(word)


with open('exercise6.yml', 'w') as e:
    e.write(yaml.dump(final_list, default_flow_style=False))

with open('exercise6.json', 'w') as f:
    json.dump(final_list, f, indent=4)

