import requests

BASE = "http://127.0.0.1:5000"

for i in range(5):
    print(i)


response = requests.put(BASE+"/video/1", {"likes": 10, "name": "Tim", "views": 100})
print(response.json())
input()
response = requests.get(BASE+"/video/2")
print(response.json())

# response = requests.put("%s/video/1" % BASE, {"likes": 10})

# name = "daniel"
# age = 40
# response = requests.get("{0}/helloworld/{1}" .format(BASE, name))
#response = requests.get("{0}/helloworld/{1}/{2}" .format(BASE, name, str(age)))
# response = requests.get(BASE + "/helloworld/daniel/40")
#response = requests.post(BASE + "helloworld")
# print(response.json())
