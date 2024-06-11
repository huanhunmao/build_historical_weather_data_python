import requests

API_URL = 'https://api.deepsource.io/v1/gh/github/huanhunmao' \
          '/build_historical_weather_data_python/'
API_TOKEN = 'xxx'


def get_repo_info():
    headers = {
        'Authorization': f'Token {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        repo_info = response.json()
        print("Repository info fetched successfully:")
        print(json.dumps(repo_info, indent=4))
    else:
        print('Error fetching repository info')
        print(response.status_code, response.text)


if __name__ == '__main__':
    get_repo_info()
