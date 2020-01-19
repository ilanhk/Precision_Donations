import requests  #dont forget to pip install requests
import json
from pprint import pprint




response = requests.get('https://disease-info-api.herokuapp.com/diseases')



data = json.loads(response.content)

pprint(len(data['diseases']))
pprint(data['diseases'][2]['name'])