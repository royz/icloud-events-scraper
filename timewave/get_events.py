import requests

cookies = {
    'ext_name': 'ojplmecpdpgccookcobabopnaifgidhf',
    'timewave_session': '5f0dbe5d98fb48fe5757f7b8a136be7a58eadc57%2BQf5HLphUniUlJriagCLxUFb5GZz2zKewHsXH9Pqo',
    'login-username': 'c6ca35eac8fb0a44cdf7743f789936deaaa24fe4%2BR-test',
    'session_payload': '281378cc22e200617a69a267a7f28c4ee90bad44%2BeyJpdiI6IldaV1A3QVFYWUZ6SjkxakZCNTFsV1E9PSIsInZhbHVlIjoiUjdsemhGblhYZmgzcXBPck13d1A4SFBLb3ArQkh5bndZeUorT1MySndzQzFpdm5SVWczTnJrS25Nd1dRd3NXbWhtWTN0YU5GU3hLbTYxRk5GT0Z6ZHpuVEZ5MmFlYkMwT0Uxd1V1NGVkMVFydjFNMTk3TTNkUWlUbEt3WUVHM1dEdVlWaWhvdHFGbTNWREs2MjZydnk2TG82a0ZXNU1pUVBMQWxXRGFQYjdUc3IrR0tUR2d4WG85NjRCRThpdEgySVlYblNScTFxXC85RlwvejRvQUdxOEZ0QktLSjhJY0xGbThPNllnS2ZobzZsNzNqbCtFaWN4SkZ0V1JGUFpnUUhZeWJZaExcL25Bc2N1ZDRPMHJkUk1jSmFpNks2QzFBWnBoWkRtV2kyaTRtZkJqbEJzclhSYXRCcVZqeXRXOWxwVTdUVWJjZ0VwejVcL0M2TVFzQlptUW9BcTE1ZlpLbmVBbnN0WFpHXC92aVRtU1B1NXhDdFdveEhjQmJnQnlFQVh4S0ZFbXc3ZDc2U2NWbGZcLzN3Rm5zTlwvRThsK1BsbUZDSUlibXlQYzhJbFZKcVE9IiwibWFjIjoiM2Y4MDc4ZmRmYmFjNjlhNGQyNmE1YzQyOGIzMmUxYTFiZjg3ZWFlYTBkMmM4ODk2MmFmZGExM2Y0YmJmMjI5NCIsInNhbHQiOiI1ZjkxLWRjNGE1Y2YwZSJ9',
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
    'Referer': 'https://stadjatten.timewave.se/schedule/month?s_date=2020-09-26&z_search=load&pt=0',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,sv;q=0.6',
}

params = (
    ('z_search', 'load'),
    ('pt', '0'),
    ('s_date', '2020-09-26'),
)

response = requests.get('https://stadjatten.timewave.se/schedule/month', headers=headers, params=params,
                        cookies=cookies)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
