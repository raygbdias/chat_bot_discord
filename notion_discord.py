import requests, json
from discord_webhook import DiscordWebhook

with open("token.json") as jFile:
    token = json.load(jFile)

base_url = "https://api.notion.com/v1/databases/"
database_id = token["database_id"]

header = {
            "Authorization": token["token"],
            "Notion-Version": "2021-08-16"    
        }

query = {
    "filter":
    {
        "property": "Bool",
        "checkbox":
        {
            "equals": True
        }
    }
}

#response = requests.get(base_url + database_id, headers=header, data=query)
response = requests.post(base_url + database_id + "/query", headers=header, data=query)

def dict_decoder(x):
    return [i for i in x]

"""titulo = response.json()["title"][0]["text"]["content"]
print(titulo)

properties = response.json()["properties"]

for coluna in properties:
    link = response.json()["properties"][coluna]["name"]
    print(link)"""


#print(response.json())

link = response.json()["results"][0]["properties"]["Link"]["url"]
nome = response.json() ["results"][0]["properties"]["Nome"]["rich_text"][0]["text"]["content"]
print(link, nome)

data = {
            "content": link + "\n" + nome,
            "username": "Captain Hook"
        }

requests.post(token["discord_webhook"], data)

if response: 
    print(f"{response} Conexão bem sucedida!")



"""webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/" + token["discord_id"] + "/" + token["token_webhook"],
    content= nome + "\n" + link,
    username="Captain Hook")

response = webhook.execute()
"""

"""file = open("data.json", "w")
json.dump(response.json(), file, indent=2)"""