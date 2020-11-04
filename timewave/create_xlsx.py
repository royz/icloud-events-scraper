import csv
import json
import re


def parse_pn(pn: str):
    pn = pn.replace(' ', '').replace('-', '')
    if len(pn) > 10:
        pn = pn[-10:]
    pn = pn[:6] + '-' + pn[6:]
    return pn


def parse_phone(num):
    num = num.replace(' ', '').replace('-', '').strip().removeprefix('+')

    if num.startswith('0'):
        num = '+46 ' + num[1:]
    elif num.startswith('46'):
        num = '+46 ' + num[2:]
    print(num)
    return num


def parse_address(addr):
    return ' '.join(addr.split())


def parse_header(header):
    new_hd = header.replace('*', '').replace('#', '').strip()
    return new_hd


with open('timewave.json', encoding='utf-8-sig') as f:
    data = json.load(f)
FROM = ['från 1', 'från1', 'från', 'adress', 'stopp 1', 'adress 1', 'adress1', 'stopp1', 'stopp']
TILL = ['till', 'till2', 'till 2', 'stopp2', 'stopp 2', 'adress2', 'adress 2']
HEADLINES = ['flytthjälp', 'flyttstädning', 'flyttstäd',
             'storstädning', 'pack', 'bärhjälp', 'flytt', 'bortforsling']
parsed_data = [
    ['Id', 'Header', 'Name', 'Person Number', 'Email', 'Date', 'Fran', 'Till',
     'Phone', 'städjätten/flyttgubbarna', 'person number & phone', 'email & till']
]

for event in data:
    try:
        title = event['header']
        description = event['description']
        date = event['date']

        if 'städjätten' in title.lower():
            col9 = 'städjätten'
        elif 'flyttgubbarna' in title.lower():
            col9 = 'flyttgubbarna'
        else:
            col9 = None

        col10 = None
        col11 = None

        user_number = None
        phone = None
        name = None
        fran = None
        till = None
        email = None

        for i, line in enumerate(description):
            # get the user number
            if not user_number:
                try:
                    user_number = parse_pn(re.findall(r'^(?!0|46|\+)[0-9- ]{10,}', line)[0])
                    # get the name
                    name = description[i - 1]
                except:
                    pass

            if not email:
                # get email
                # regex: [a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+
                emails = re.findall(r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+', line)
                if len(emails) > 0:
                    email = emails[0]

            if not phone:
                # get  phone number
                # regex: (0|46|\+)[0-9- ]{6,}
                phones = re.findall(r'\b(0|46)([0-9- ]{6,})\b', line)
                if len(phones) > 0:
                    phn = ' '.join(phones[0]).strip().removesuffix('-').replace(' ', '').strip()
                    if '775552222' in phn or '81214410' in phn:
                        pass
                    else:
                        phone = ' '.join(phones[0]).strip().removesuffix('-').strip()

            # get fran
            if not fran:
                try:
                    for fn in FROM:
                        if line.lower().startswith(fn):
                            fran = line[len(fn):].removeprefix(':').strip()
                            break
                except:
                    pass

            # get till
            if not till:
                try:
                    for tl in TILL:
                        if line.lower().startswith(tl):
                            till = line[len(tl):].removeprefix(':').strip()
                            break
                except:
                    pass

        if not user_number or not phone:
            col10 = 'not completed'
            col11 = 'not completed'

        if not email or not till:
            col10 = 'not completed'

        parsed_data.append([
            event['bid'], parse_header(title), name, user_number, email, date, parse_address(fran),
            parse_address(till), parse_phone(phone), col9, col10, col11
        ])
    except:
        pass

with open('timewave.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for row in parsed_data:
        writer.writerow(row)
