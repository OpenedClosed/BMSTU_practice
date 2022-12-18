import pickle

import requests

users_response = requests.get('https://jsonplaceholder.typicode.com/users/')
users = (users_response.json())
BASE_URL = 'https://webhook.site/4cd31630-1f2f-431e-a481-98c155f1ad77'

answer = []
for user in users:
    user_id = user['id']
    user_email = user['email']
    user_posts = requests.get(f'https://jsonplaceholder.typicode.com/posts?userId={user_id}').json()
    user_comments = [comment for comment in requests.get('https://jsonplaceholder.typicode.com/comments').json() if comment['email'] == user['email']]
    comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()
    answer.append({
        "id": user_id,
        "username": user['username'],
        "email": user_email,
        "posts": len(user_posts),
        "comments": len(user_comments)
    })

statistics_json = {"statistics": answer}

response = requests.post(BASE_URL, json=statistics_json)
with open("solution.pickle", 'wb') as f:
    pickle.dump(response, f)
