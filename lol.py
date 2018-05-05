import requests

apikey = "trnsl.1.1.20180428T041831Z.86040fd392d3a4f4.26eec88255a446984238ac823efdb29e4b8e9661"
lng = 'ru-en'

lngs = ["ru", "en", "kk"]
names = ["Русский", "Английский", "Казахский"]

def fromPrint:
    for lng1 in names:
        print(names.index(lng1) + 1, lng1)
    lng = lngs[int(input("from: ")) - 1]

for lng1 in names:
    print(names.index(lng1) + 1, lng1)
lng += "-"
lng += lngs[int(input("to: ")) - 1]

data = {
                'key' : apikey,
                'text' : input("text: "),
                'lang' : lng,
                'format' : 'plain'
            }
answer = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data)
dictionary = answer.json()
print(dictionary["text"][0])
