# Modules import
from datetime import datetime
import modules.log as log
import logging
import json
import modules.collect as c
import pandas as pd


BOARD_ID='60bbbe49a7dc5a872b65fb75'
URL_BOARD_LIST='https://api.trello.com/1/boards/' + BOARD_ID + '/lists'
URL_CARDS_IN_LIST_BASE = "https://api.trello.com/1/lists/"
URL_CARDS_IN_LIST_SUFIXE = "/cards"
URL_ACTIONS = "https://api.trello.com/1/cards/"
URL_ACTIONS_SUFIXE = "/actions"

QUERY = {
   'key': 'f58789ac686428e7e03ea0020455d382',
   'token': 'e3244c44878dadefb3acf8ab1399edbb36a65e996a4bc3c4f9235ebf258d6f6b'
}
HEADERS = {
   "Accept": "application/json"
}


def main():
   try:
      print(' ----- Fetch data about trello board -----')
      print(URL_BOARD_LIST)
      print('')
      lists = c.fetch_trello_api(URL_BOARD_LIST, HEADERS, QUERY)

      print(' Trello board lists:\n')
      for list in lists:
         print('- List name {} : List id {}'.format(list['name'], list['id']))
      print('')

      for list in lists:
         print(' The list {} has this cards: '.format(list['name']))
         cards = c.fetch_trello_api(URL_CARDS_IN_LIST_BASE + list['id'] + URL_CARDS_IN_LIST_SUFIXE, HEADERS, QUERY)

         for card in cards:
            print('     - {}: {}\n'.format(card['name'], card['id']))
            actions = c.fetch_trello_api(URL_ACTIONS + card['id']+ URL_ACTIONS_SUFIXE, HEADERS, QUERY)
            print(URL_ACTIONS + card['id']+ URL_ACTIONS_SUFIXE)
            
            for action in actions:
               print(json.dumps(action, sort_keys=True, indent=4, separators=(",", ": ")))
               dados = json.dumps(action, sort_keys=True, indent=4, separators=(",", ": "))
      print(type(dados))

   except Exception as e:
      logging.exception(e)


   finally:
        log.end_logging()


if __name__ == '__main__':
    log.start_logging()
    main()

#print('Card "{}"" foi criado em: {}'.format(card['name'], utc_creation_time))


