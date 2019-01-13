import requests


url = 'https://api.github.com/rate_limit'
r = requests.get(url)
print(r.json()['resources']['search'])
