import base64
from constants import constants

class data:
    def __init__(self, name, link, credential):
        self.name = name
        self.link = link
        self.credential = credential

lists = []

def convertBase64(credential):
    credential_string = credential
    credential_string_bytes = credential_string.encode("ascii") 
    
    base64_bytes = base64.b64encode(credential_string_bytes) 
    base64_string = base64_bytes.decode("ascii") 

    return base64_string

for item in constants:
    lists.append(data(item["name"], item["link"], convertBase64(item["credential"])))

def displayOptions():
    for index, list in enumerate(lists):
        print(f"{index + 1} - Name: {list.name}")

def options():
    displayOptions()
    selected = input("Choose: ")

    return lists[int(selected) - 1]
    