import requests
import json

headers = {
    'authority': 'p51-calendarws.icloud.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'dnt': '1',
    'content-type': 'text/plain',
    'accept': '*/*',
    'origin': 'https://www.icloud.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.icloud.com/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,sv;q=0.6',
    'cookie': 'X_APPLE_WEB_KB-LVGVFZDVC0XQJPYEJQT7P9PS8T4="v=1:t=AQ==BST_IAAAAAAABLwIAAAAAF9kl1URDmdzLmljbG91ZC5hdXRovQDucmPgzmLFSq38dqvtb6XpqnBaBnmCJnYfyd9MJ_MyQTinb_V0ZW4cont0fB7V8Gqo9V3nkDTCPdoG1IcIAw6ZSHdZhktVKWLV66UdWN-xIVI_nERs6Sb3Xsao89oyLQ61CWTYLLNrJh3rxDVJBSBvgysqvA~~"; X-APPLE-WEBAUTH-HSA-TRUST="ed178342c9855c57b2cf74d5abf9dc808bc06e395eca108833fe16a3311f749f_HSARMTKNSRVXWFla1uzSzFWbfp8v7/JKQRSN+w7T2cwjjxUoesS29V8EGmBmXtz9o8B+SBfiWTgURjx000CpOxkzK2/PmyMXityhOpo09wrk15c/AkKUDc168uPHQ967hG52PXkiSRVX"; X-APPLE-WEBAUTH-PCS-Documents="TGlzdEFwcGw6MTpBcHBsOjE6AX67K2gqhqTQ/HByeoHyStfHx8jUT+OGrSrAyIgE9LSRcacCETQ+rJGNiONOXGDGe4z3QI+tBu0kzhzFK76J2uZ2AxNu1vlJEnwUZCoXYcstta999C4fvjfsMVPOVZP718HJVJ6Zb7K0PZy8DcGQzb5PIwt8B3oef6vjGDfOQleVqQ/Gc2MgjA=="; X-APPLE-WEBAUTH-PCS-Photos="TGlzdEFwcGw6MTpBcHBsOjE6AaKenhLEaZeSz2EVO068HTkCLtXs0ffYmJxgreBksIaPlKUtA4oTlTPccoS0q9EeHUPAwopGK9g21VIZNSR4S9XtQYcUA8H+9uFcgZQR3jvrJzG/Lrode4k/UbNuH9rSfp1LhruhVWOoYqCLRTmOIQTGyKrp2jQbSYVc8w2cBxydyTVqrd0fog=="; X-APPLE-WEBAUTH-PCS-Cloudkit="TGlzdEFwcGw6MTpBcHBsOjE6Ac/t06fZVbOc29W0f6FyCOIadS1XZaxo9oAT2wcwuXAOm2/wy/R/KSIbLANHIBz65fW+778tAdz8IqOMhbRDPHMAqawjPFdTpEvTCCADEx6tnukQV+V41ZLQTFcpFbBKsAm3xOFUbiydA4MzOquN8+xyf85qowYWgEwusnnjvxWnTKX142nhJg=="; X-APPLE-WEBAUTH-PCS-Safari="TGlzdEFwcGw6MTpBcHBsOjE6Ab3bflUpIc/hZhxUWm99QV1eyAgAFPvznzwVXdr5Jv4yLPEe/HeBXo3SHtH+X8tXYogfNsefcR02GYynpwaqdrNU1wUt9bQmfKVoHYPmFZsx99haELDzGM86MQXZaNzA3qo6DJNWTgo2FaDW4iydY1Ecyc90NpQ/RO7l1EMogvJjinIzccMIrg=="; X-APPLE-WEBAUTH-PCS-Mail="TGlzdEFwcGw6MTpBcHBsOjE6ARR1piEXkqo4HHmspUQruEvGMa9dbi4vZffsRj0k1YGTfHaBJ9BbR1k2/ihj5vnUTvX+ObIIcxN5Vh74hytgA3NizHvG8d3Xqy07JuuWkuwaeOOQpwwjn1bxtmPZ2F9lSpoCpFCxmNnfR8VzE/qUo0XsD/K3LB6KvV9Lx+QK6Ygg5OEOT06xEw=="; X-APPLE-WEBAUTH-PCS-Notes="TGlzdEFwcGw6MTpBcHBsOjE6AcY3gJTFxCm4iiwrrEghf3norHMd7A3s/DhQg0YuUSVM2gbMzKqLd7E2TNtwWtyTRQ+j4vlB4pg6zLGN4S+MYqGlAzdWgfwXT1V5rmIWNt3OZPgLRE7Md9dkSt9adP/Nf5NcgL0wLeZmU1v73oi4l1n9YjZegbjbJqYSi6lNiDh49Bi5H0ykUQ=="; X-APPLE-WEBAUTH-PCS-News="TGlzdEFwcGw6MTpBcHBsOjE6AZvqZ+khNdGIBgMlCMmrVUvuO5mLallyRVX2t2nK532l8LuQo0iS9cX7KrQSd40q+MN6/TNNTtQQYVwp3sTVlZF5Bp+mE/voayL7b7NR9A7bwKONO2tFYlA8LC47rosdAs7ux5Xc26V+LFr95/havbtVR8WzV/UlOu+xjVY7/m04SpXY97mT/Q=="; X-APPLE-WEBAUTH-PCS-Sharing="TGlzdEFwcGw6MTpBcHBsOjE6ATT7lzMkLEQN21Hr7iICUDbhV9ZKZk5/kkZkg/3ZDozgNMZzS8ZWO2IJmYmdMhuqMXW8wW98hqdGMXRwIkxE+asnsAg9If0pynemWwqAzebvAeRFCCCW1Pt06ZD8JMsaq+tx51Zm0EOynuAVWPd6G4I5SgLX1T0QMT6XGxFHvQdLSb6mqIlGiA=="; X-APPLE-WEBAUTH-USER="v=1:s=1:d=11613995326"; X-APPLE-WEB-ID=DC94181F502DEC3DA623FE6267923A8455022017; X-APPLE-WEBAUTH-VALIDATE="v=1:t=BQ==BST_IAAAAAAABLwIAAAAAF-XHnURDmdzLmljbG91ZC5hdXRovQC_x_GfE1Xpmliulvs9O1iKLnhAu6Dd4m5r8iySk70tkBGNmHQUAz2LBEQbMAhyBnymirecRZPZn7OHq5Z_TatDxxHQYtvShh9HddUaKrb-KZKFAjwgaMIYvA2BGc5OCD_OZwCC7Z-CyRvd2ZM_sjPfpwzKFw~~"; X-APPLE-WEBAUTH-TOKEN="v=2:t=BQ==BST_IAAAAAAABLwIAAAAAF-XIV4RDmdzLmljbG91ZC5hdXRovQArRZDJrQGXN76xi5sN5szZPlgwFQ118wXZHyH3WZH8JndxKrusqyf8l2K84_GUqZ8a8h_OviZaTzHHFVhArxn0qtrOms00jUPrWuIjQro5vH_deGsGl2wJnnUOtxlmUReBsQLijiexhvYvIZ62_676oWSyOw~~"',
}

params = {
    'clientBuildNumber': '2019Project30',
    'clientId': '08a5689c-6326-4767-80fb-dc092c3888d3',
    'clientMasteringNumber': '2019B35',
    'clientVersion': '5.1',
    'dsid': '11613995326',
    'endDate': '2020-08-31',
    'lang': 'en-us',
    'requestID': '15',
    'startDate': '2017-02-01',
    'usertz': 'US/Pacific',
}

response = requests.get('https://p51-calendarws.icloud.com/ca/events', headers=headers, params=params)
print(response)
print(response.text)
with open('ical.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, indent=2)
