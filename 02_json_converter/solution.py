import os
import json
import csv

with open('users.csv', encoding='utf-8') as f:
    users = list(csv.DictReader(f))

with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f)