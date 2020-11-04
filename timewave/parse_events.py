import json
import openpyxl
from bs4 import BeautifulSoup
import glob


def parse_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # data_table = soup.find('table', {'id': 'schedule-container'}).find('tbody')
    schedules = soup.find_all('div', {'class': 'schedule-event-container'})
    events = []
    for schedule in schedules:
        date = schedule['date']
        bid = schedule['bookingid']
        eid = schedule['employeeid']
        header = schedule.find('a').text.strip()
        description = list(schedule.stripped_strings)
        print(header)
        events.append({
            'bid': bid,
            'eid': eid,
            'date': date,
            'header': header,
            'description': description,
        })
    return events


if __name__ == '__main__':
    data = []
    files = glob.glob('data2/*.html')
    for file in files:
        ev = parse_file(file)
        print('-' * 100)
        data.extend(ev)

    with open('timewave.json', 'w', encoding='utf-8-sig') as f:
        json.dump(data, f, indent=2)
