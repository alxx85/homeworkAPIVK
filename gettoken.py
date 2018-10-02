from urllib.parse import urlencode

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

print('?'.join((OAUTH_URL, urlencode(oauth_data))))
