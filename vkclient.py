import requests
import constants


class User:
    """ Класс для экземпляров описывающих пользователей VK и реализующий поиск общих друзей
       Экземпляр класса создается на основе идентификатора пользователя VK"""

    def __init__(self, user_id):
        self.token = constants.TOKEN
        self.user_id = user_id

    def __str__(self):
        return 'https://vk.com/id' + str(self.user_id)

    def get_params(self):
        return {
            'access_token': self.token,
            'user_id': self.user_id,
            'v': '5.85'
            }

    def get_info(self):
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/users.get', params)
        print(response.json()['response'][0])

    def __and__(self, other):
        parametrs = {
            'access_token': self.token,
            'source_uid': self.user_id,
            'target_uid': other.user_id,
            'v': '5.85'
            }
        response = requests.get('https://api.vk.com/method/friends.getMutual', parametrs)
        list_id = list()
        for id in response.json()['response']:
            list_id.append(User(id))
        return list_id


# Создаем двух пользователей, выводим ссылку на страницу, сравниваем списки друзей, добавляем
# общих друзей в список, выводим Фамилию, ID и Имя для общих друзей
Alx = User(constants.USER_ID)
Alx.get_info()
Mari = User(constants.USER2_ID)
Mari.get_info()
friends_list = Alx & Mari
if len(friends_list) != 0:
    print('Общие друзья двух пользователей:')
    for friend in friends_list:
        friend.get_info()
else:
    print('Общих друзей нет...')
print(Alx)
