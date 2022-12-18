import requests
import pickle

users_response = requests.get('https://jsonplaceholder.typicode.com/users/')
users = (users_response.json())
BASE_URL = 'https://webhook.site/4cd31630-1f2f-431e-a481-98c155f1ad77'

answer = []
for user in users:
    user_id = user['id']
    user_email = user['email']
    user_posts = requests.get(f'https://jsonplaceholder.typicode.com/posts?userId={user_id}').json()
    # user_comments = [comment for comment in requests.get('https://jsonplaceholder.typicode.com/comments').json() if comment['postId'] in user_posts]
    user_comments = [comment for comment in requests.get('https://jsonplaceholder.typicode.com/comments').json() if comment['email'] == user['email']]
    comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()
    # print(user['email'])
    # for comment in comments:
    #     if user['email'] == comment['email']:
            # print(comment['email'])
    answer.append({
        "id": user_id,
        "username": user['username'],
        "email": user_email,
        "posts": len(user_posts),
        "comments": len(user_comments)
    })
    # print(user_comments)
# print(answer)

s = {"statistics": answer}

# print(answer)
response = requests.post(BASE_URL, json=s)
with open("solution.pickle", 'wb') as f:
    pickle.dump(response, f)
