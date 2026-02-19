import requests

url = "https://fr.wikipedia.org/wiki/Coupe_du_monde_de_football_2026#Stades"
response = requests.get(url)
html_content = response.text

print(html_content)