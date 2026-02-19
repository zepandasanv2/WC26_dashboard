import requests

url = "https://fr.wikipedia.org/wiki/Coupe_du_monde_de_football_2026#Stades"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
response = requests.get(url, headers=headers)
html_content = response.text

print(html_content)