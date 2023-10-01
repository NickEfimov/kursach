import json

with open('operations.json', 'r', encoding='utf8') as file:
    operations = json.load(file)
    executed_operations = list(filter(lambda x: x['state'] == 'EXECUTED', operations))
sorted_data = sorted(executed_operations, key=lambda x: x['date'], reverse=True)
for item in sorted_data[:5]:
    print(item)