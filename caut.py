import json

with open('data.json') as file:
  a = json.load(file)
  
  for b in a:
    caut = "память"
    if caut in b['titlu']:
      print(b)