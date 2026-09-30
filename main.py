import requests
import csv
import json



# code for csv.file

import requests
import csv

url = "https://v2.jokeapi.dev/joke/Any"

response = requests.get(url)
data = response.json()

print("Category:", data["category"])

if data["type"] == "single":
    joke = data["joke"]
else:
    joke = data["setup"] + " " + data["delivery"]

print("Joke:", joke)

with open("joke.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Category", "Joke"])
    writer.writerow([data["category"], joke])




# code for json.file 

# url = "https://v2.jokeapi.dev/joke/Any"
# response = requests.get(url)
# data = response.json()

# with open("joke.json", "w") as file:
#     json.dump(data, file, indent=4)

# print("Joke saved to joke.json")



# code for joke.output

# url = "https://v2.jokeapi.dev/joke/Any"
# response = requests.get(url)
# data = response.json()

# # print(data)
# print("category:",data["category"])

# if data["type"] == "single":
#     print("joke:" , data["joke"])
# else:
#     print("setup",data["setup"])
#     print("delivery:" , data["delivery"])

