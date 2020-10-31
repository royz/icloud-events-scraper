import json
import csv
import re
import pprint

HEADLINES = ['flytthjälp', 'flyttstädning', 'flyttstäd',
             'storstädning', 'pack', 'bärhjälp', 'flytt', 'bortforsling']
TILL = ['till', 'till2', 'till 2', 'stopp2', 'stopp 2', 'adress2', 'adress 2']


def parse_pn(pn: str):
    pn = pn.replace(' ', '').replace('-', '')
    if len(pn) > 10:
        pn = pn[-10:]
    pn = pn[:6] + '-' + pn[6:]
    return pn


with open('ical.json', encoding='utf-8') as f:
    data = json.load(f)

parsed_data = [
    ['Id', 'Header', 'Name', 'Person Number', 'Email', 'Date', 'Address', 'Till', 'Phone', 'städjätten']
]

for event in data['Event']:
    try:
        guid = event['guid']
        title = event['title']
        # print(title)
        address = event['location'].replace('\n', ', ')
        description = event['description']
        start_date = event['localStartDate']
        date = f'{start_date[3]}-{start_date[2]}-{start_date[1]}'

        # check the title
        if not any([headline in title.lower() for headline in HEADLINES]):
            continue

        # get email
        # regex: [a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+
        emails = re.findall(r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+', description)
        if len(emails) > 0:
            email = emails[0]
        else:
            email = ''

        # get  phone number
        # regex: (0|46|\+)[0-9- ]{6,}
        phones = re.findall(r'\b(0|46)([0-9- ]{6,})\b', description)

        try:
            phone = f"{' '.join(phones[0])}".strip().removesuffix('-').strip()
        except:
            phone = ''

        user_number = None
        name = None
        till = None
        lines = [line.strip() for line in description.split('\n') if line.strip() != '']
        for i, line in enumerate(lines):
            # get the user number
            if not user_number:
                try:
                    user_number = parse_pn(re.findall(r'^(?!0|46|\+)[0-9- ]{10,}', line)[0])
                    # get the name
                    name = lines[i - 1]
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
        parsed_data.append([
            guid, title, name, user_number, email, date, address, till, phone, 'städjätten'
        ])
    except:
        pass

with open('ical.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for row in parsed_data:
        writer.writerow(row)
