import requests

link = "http://data.egov.kz/api/v2/valutalar_bagamdary4/v307"

response = requests.get(link)

dictionary = response.json()
print(dictionary[2]["kurs"])

