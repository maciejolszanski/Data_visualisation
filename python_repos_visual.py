import requests


url = "https://api.github.com/search/repositories?q=language:python&sort=starts"

headers = {'Accept': 'aplication/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Kod stanu: {r.status_code}")

response_dict = r.json()
print(f"Całkowita liczba repozytoriów: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Liczba zwróconych repozytoriów: {len(repo_dicts)}")

