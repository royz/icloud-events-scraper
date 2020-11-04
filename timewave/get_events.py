import requests
import datetime
import os
from dateutil import relativedelta


def get_page(date):
    cookies = {
        'ext_name': 'ojplmecpdpgccookcobabopnaifgidhf',
        'timewave_session': 'df891fb934fc8ddaa98b898ba20af94b1309ad51%2Bp1JR4t8uDcRKmyKwwd8CWtrgBFHFIEVjclIGPGUd',
        'login-username': 'c6ca35eac8fb0a44cdf7743f789936deaaa24fe4%2BR-test',
        'session_payload': '8732d19e065de21954ab2d700928e7b8fcfd47bc%2BeyJpdiI6IkV4dzlnUCtHZ21HVmYxZTc5ZHhtelE9PSIsInZhbHVlIjoiQ3F1XC9MNmlaMkhlbTVGQkYwNHJrdndKb2NieWlUYjVYUkJyWHpGaHlyRFJTVkJXTmpCaWZGWGFVaUx6NzJSbDhoY2M3eGNNMUVUOXlwaHZEM0RlSThleDVDTnJLMG5kMHF3dTBXWUNoWmlUN0tpUHlwRGRqK0pjXC9taEhLVE42SVRSSnFlUlFuK1ZlRFBFT1RVbmZUWjM0UGwxczNJWEs5K0JLdEg0WWdxZ1ZpMmo1UFdaelJheDhqMmpqWnVjeEtVVkZxWVZuVG9MbzFxS1NkdDZTXC9DTW94RVA5Tm1UcG40c1ZkWlJIU200R3RGaElCZHd3Y0Z0TFFNczVjem53VU9jcGRxT1pmTGVRaXlNNVZyNFZmenRxcFJMOFFKQ0MxTTgzSG5QR0xMaTU1SXVXdnZoWUkrc1FFUDFBaDdJQnpFRlhVRU5saGs3dzJcL2MzSXdmQmlpVDVIVmRNbFlRTDJWQzh5S2drOHNwdWFZaW9OcThkak1qVU9VdHBCU3NjZ2cxUUhiQnlWQ3NpNWlqNFRJK1ZDbXhUYzhKekdzUGFFZUh4SXQ1N2hCcDg9IiwibWFjIjoiMmQ3MWJiOTA5ODYzYWU3ODFhMGEwOGNiNWI4MmNhODI3ZDVjYzU1OGRhYWExNTIwNjdhODQ0ZmYyMDg4MzBjYSIsInNhbHQiOiI1ZjkxLWRjNGE1Y2YwZSJ9',
    }

    headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://stadjatten.timewave.se/schedule/week',
        'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,sv;q=0.6',
    }

    params = {
        'z_search': 'load',
        # 'pt': '44439',
        's_date': date,
    }

    response = requests.get('https://stadjatten.timewave.se/schedule/month', headers=headers, params=params,
                            cookies=cookies)
    # print(response)
    with open(f'data2/{date}.html', 'w', encoding='utf-8') as f:
        f.write(response.text)


current_date = datetime.date(day=1, month=1, year=2019)
end_date = datetime.date(day=2, month=9, year=2020)

while current_date <= end_date:
    date_str = current_date.strftime('%Y-%m-%d')
    file_name = f'{date_str}.html'
    if os.path.exists(file_name):
        continue

    get_page(date_str)
    print(file_name, 'saved')
    current_date = current_date + relativedelta.relativedelta(months=1)
