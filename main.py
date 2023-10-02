import json
from utils import date_reformat, blurer, second_string

with open('operations.json', 'r', encoding='utf8') as file:
    operations = json.load(file)
    executed_operations = list(filter(lambda x: x.get('state') == 'EXECUTED', operations))
    sorted_data = sorted(executed_operations, key=lambda x: x['date'], reverse=True)
    for item in sorted_data[:5]:
        currency = (item['operationAmount']['currency']['name'])
        date = date_reformat(item['date'])
        desc = (item['description'])
        sender = item.get('from', '-')
        fromfrom = second_string(sender)
        reciever = second_string(item['to'])
        amount = item['operationAmount']['amount']
        print(f'{date} {desc}\n{fromfrom} -> {reciever}\n{amount} {currency}\n')