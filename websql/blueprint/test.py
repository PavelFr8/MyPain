from requests import get, post, delete


from requests import get, post, delete

'''
print(get('http://localhost:8080/api/v2/news').json())
print(get('http://localhost:8080/api/v2/news/1').json())

print(get('http://localhost:8080/api/v2/news/999').json())
print(post('http://localhost:8080/api/v2/news', json={}).json())

print(post('http://localhost:8080/api/v2/news',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:8080/api/v2/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())

print(delete('http://localhost:8080/api/v2/news/999').json())
# новости с id = 999 нет в базе
'''
print(post('http://localhost:8080/api/v2/users',
           json={'name': 'Заголовок',
                 'about': 'Текст новости',
                 'email': '1@11131111',
                 'hashed_password': '123'}).json())
