import requests

# url = "https://jsonplaceholder.typicode.com/posts"
# params = {'userId': 1}

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()

#     print("Eerste bericht gebruiker", data[0])

# else:
#     print(f"Er is iets misgegaan. Statuscode: {response.status_code}")


#-------------------------------------

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": "Iets dom",
#     "body": "Dit is totaal nutteloos.",
#     "userId": 1
# }

# response = requests.post(url,json=data)

# if response.status_code == 201:
#     post = response.json()

#     print("Nieuw bericht", post)

# else:
#     print(f"Er is iets misgegaan. Statuscode: {response.status_code}")

#---------------------

#GET (Data ophalen)

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print(data)

# else:
#     print(f"Er is iets misgegaan. Statuscode: {response.status_code}")

# #POST (Data versturen)

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": "test",
#     "body": "Dit is de inhoud van een nieuwe post",
#     "userId": 1
# }

# response = requests.post(url, json=data)

# if response.status_code == 201:
#     data = response.json()
#     print(data)

# else:
#     print(f"Er is iets misgegaan. Statuscode: {response.status_code}")

# #-------------------------------
# #Patch (Data gedeeltelijk aanpassen)

# url = "https://jsonplaceholder.typicode.com/posts/1"
# data = {
#     "title": "Deel 2 van update post",
# }

# response = requests.patch(url, json=data)

# if response.status_code == 200:
#     data = response.json()
#     print(data)

# else:
#     print(f"Er is iets misgegaan. Statuscode: {response.status_code}")



# #-------------------------------
# #PUT (Data volledig aanpassen)

# url = "https://jsonplaceholder.typicode.com/posts/1"
# data = {
#     "title": "Deel 2 van update post",
#     "id": 1,
#     "body": "Dit is de geupdatete inhoud van de post",
#     "userId": 1
# }

# response = requests.put(url, json=data)

# if response.status_code == 200:
#     data = response.json()
#     print(data)

# else:
#     print(f"Er is iets misgegaan. Statuscode: {response.status_code}")

#-------------------------------
#DELETE (Data verwijderen)

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

if response.status_code == 200:
    print("Post is succesvol verwijdert.")

else:
    print(f"Er is iets misgegaan. Statuscode: {response.status_code}")