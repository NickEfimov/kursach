def blurer(number):
    digits = ''.join(str(i) for i in number)
    if len(digits) == 16:
        card_number = digits
        c_masked_number = card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[-4:]
        return c_masked_number
    if len(digits) == 20:
        account_number = digits
        a_masked_number = "**" + account_number[-4:]
        return a_masked_number


def second_string(data):
    '''data = "значение по ключу "from" or "to""'''
    parts = data.split(" ")
    number = parts[-1]
    specie = ' '.join(parts[:-1])
    return f'{specie} {blurer(number)}'


def date_reformat(date):
    '''date = значение по ключу "date"'''
    halfs = date.split("T")
    old_date = halfs[0]
    date_lst = old_date.split("-")
    new_date = '.'.join(date_lst[::-1])
    return new_date