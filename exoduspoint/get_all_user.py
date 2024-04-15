import requests

url = 'https://jsonmock.hackerrank.com/api/article_users?page='

results = []

def get_page(page_number, threshold):
    response = requests.get(url + str(page_number)).json()
    users = response['data']
    results.extend([user['username'] for user in users if user['submission_count'] > threshold])
    # get remaining
    if page_number < response['total_pages']:
        get_page(page_number+1, threshold)


get_page(1, 196)
print(results)