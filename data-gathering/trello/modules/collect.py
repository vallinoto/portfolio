'''
    This python file is based on Atlassian Documentation, published in https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/

'''

import requests
import json
# import pytz
from datetime import datetime


def fetch_trello_api(url, headers, query):
   response = requests.request(
      "GET",
      url,
      headers=headers,
      params=query
   )
   return json.loads(response.text)


   
#    return pytz.utc.localize(datetime.fromtimestamp(int(card['id'][0:8],16)))
#    return (json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
