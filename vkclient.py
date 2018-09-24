import requests
from urllib.parse import urlencode
from pprint import pprint

APP_ID = 6700616
USER_ID = 25963099
USER2_ID = 235089651
OAUTH_URL = 'https://oauth.vk.com/authorize'
oauth_data = {
  'client_id': APP_ID,
  'display': 'page',
  'scope': 'status, friends',
  'response_type': 'token',
  }

#print('?'.join((OAUTH_URL, urlencode(oauth_data))))

TOKEN1 = 'eb8adca038e90af997abbf562057cda1030e9c6253d403cfab913e9a4863f852a66406a4e1c1ad477d3cd'
TOKEN = '2fc0111b6e191731ce553a52aaceb93ae85fb7a3e6452b99c445233cc198b63fd856cf3457a2024de21c7'
params = {
  'access_token': TOKEN,
  'v': '5.85'
  }
#response = requests.get('https://api.vk.com/method/users.get', params)
#pprint(response.json())


class User:

  def __init__(self, user_id):
    self.token = '2fc0111b6e191731ce553a52aaceb93ae85fb7a3e6452b99c445233cc198b63fd856cf3457a2024de21c7'
    self.user_id = user_id

  def __str__(self):
    return 'https://vk.com/id' + str(self.user_id)

  def get_params(self):
    return {
      'access_token': self.token,
      'user_id': self.user_id,
      'v': '5.85'
    }

  def get_status(self):
    params = self.get_params()
    response = requests.get('https://api.vk.com/method/status.get', params)
    self.status = response.json()['response']['text']
    print(self.status)

  def __and__(self, other):
    parametrs = {
      'access_token': self.token,
      'source_uid': self.user_id,
      'target_uid': other.user_id,
      'v': '5.85'
    }
    name = ''
    quantity = 1
    response = requests.get('https://api.vk.com/method/friends.getMutual', parametrs)
    list_id = response.json()['response']
    for id in list_id:
      name = 'User' + str(quantity)
      globals()[name] = User(id)
      print(type(globals()[name]), globals()[name])
      quantity += 1


Alx = User(USER_ID)
Mari = User(USER2_ID)
#Mari.get_status()
Alx & Mari
print(Alx)
