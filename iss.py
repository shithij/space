import requests

url= 'http://api.open-notify.org/iss-now.json'

res= requests.get(url)

loc= res.json()

print("Latitude of the ISS:",loc['iss_position']['latitude'])
print("Longitude of the ISS:",loc['iss_position']['longitude'])