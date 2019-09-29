
import requests

request = requests.get('http://api.open-notify.org')
print(request.text)
print(request.status_code)

request2 = requests.get('http://api.open-notify.org/fake-endpoint')
print(request2.status_code)

people = requests.get('http://api.open-notify.org/astros.json')
print(people.text)
people_json = people.json()
print(people_json)

#To print the number of people in space
print("Number of people in space:",people_json['number'])

#To print the names of people in space using a for loop
for p in people_json['people']:
  print(p['name'])


#Using datamuse API and query parameters
#rel_rhy keyword will tell the APIU to get the best rhyme for the specified word
parameter = {"rel_rhy":"jingle"}
request = requests.get('https://api.datamuse.com/words',parameter)

#print the first 3 words that rhyme with jingle
rhyme_json = request.json()
for i in rhyme_json[0:3]:
  print(i['word'])
