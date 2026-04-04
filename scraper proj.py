import requests
from bs4 import BeautifulSoup


try:
    request = requests.get(r"https://pixelblade.fandom.com/wiki/Codes#How_to_Redeem_Codes_in_Pixel_Blade")
    html = request.text
except Exception as e:
    print(f'An error occured, code: {e}')
    exit(1)

soup = BeautifulSoup(html, 'html.parser')
print(soup)
tags = soup.find_all('b')
data = []
codes = []

for tag in tags:
    data.append(tag.get_text(strip=True))
    

for d in data:
    if '(' and 'NEW' not in d:
        codes.append(d)

last_active = -1
for i in range(len(codes) - 1, -1, -1):
    if codes[i] == '(Active)':
        last_active = i
        break
    print()

active = codes[9:last_active]
active = [c for c in active if c != '(Active)']
expired = codes[last_active + 1:]
expired = [e for e in expired if e != '(Expired)']

while True:
    
    inp = input('What codes would you like to view? Active or expired? ')

    if inp.lower() == 'active':
        print(active)
        break
    elif inp.lower() == 'expired':
        print(expired)
        break
    else:
        print('Invalid input.')
        continue
