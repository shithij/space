import requests

url= 'http://api.open-notify.org/astros.json'

res= requests.get(url)

ppl= res.json()

print("Number of people in space right now:", ppl['number'])
print("\n")
print("List of people in space with their spacecrafts:\n")
for i in ppl['people']:
	print(i['name'],'-',i['craft'])

