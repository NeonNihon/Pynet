#!/usr/bin/env python
import yaml
import json


def open_file(f):
    with open(f, 'r') as e:
        if 'yml' in f:
            return yaml.load(e)
        if 'json' in f:
            return json.load(e)


def print_list(lst):
    for word in lst:
        print(word)


new_yaml = open_file('exercise6.yml')
new_json = open_file('exercise6.json')
print("YAML")
print("=" * 8)
print_list(new_yaml)
print("JSON")
print("=" * 8)
print_list(new_json)

