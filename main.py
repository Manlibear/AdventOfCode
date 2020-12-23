import requests
from rich import console
from art import *
from bs4 import BeautifulSoup
import os

curr_dir = os.path.dirname(__file__)
lines = open(os.path.join(curr_dir, "title.txt")).read().splitlines()

os.system("cls")

for l in lines:
    print(l)

print()

cookies = {'session': '53616c7465645f5f33ff57e38b974ce2412230184977a5d40c49a99dacf3e31c0f6ce2f06698be22144759daefe474ef'}
resp = requests.post('https://www.adventofcode.com/events', cookies=cookies)
soup = BeautifulSoup(resp.content, features="html.parser")
years = soup.body.find_all('div', attrs={'class' : 'eventlist-event'})

total_stars = 0

for y in years:
    year_name = y.a.text
    star_count = 0
    if y.span != None:
        star_count = int(y.span.text[:-1])
        total_stars += star_count
        
    # print(f"{year_name} {str(star_count).rjust(2)}/50  :star:")
    print(year_name, ("\u2B50" * star_count) + " \u2605" * (50 - star_count))

        

print()
print(f"Total: {total_stars}/{len(years) * 50} \u2B50")
print()