# Напиши решение здесь
import os
import json

count = 0


with open('server.log', encoding='utf-8') as f:
    for line in f:
        if '404' in line:
            count += 1

with open('stats.txt', 'w', encoding='utf-8') as f:
    f.write(str(count))