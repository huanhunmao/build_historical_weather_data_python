import requests
import json

# 配置你的 DeepSource 信息
DEEPSOURCE_API_URL = 'https://api.deepsource.io/v1/{provider}/{username}' \
                     '/{repo}/trigger-analyze/'
API_TOKEN = 'xxx'


def trigger_deepsource_analysis(provider, username, repo, branch='master'):
    url = DEEPSOURCE_API_URL.format(provider=provider, username=username,
                                    repo=repo)
    headers = {
        'Authorization': f'Token {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'branch': branch
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print('DeepSource analysis started successfully.')
        analysis_result = response.json()
        print(json.dumps(analysis_result, indent=4))
    else:
        print('Error starting DeepSource analysis')
        print(response.status_code, response.text)


if __name__ == '__main__':
    provider = 'github'  # 提供商名称，例如 'github'
    username = 'huanhunmao'  # 替换为你的用户名
    repo = 'build_historical_weather_data_python'  # 替换为你的仓库名

    trigger_deepsource_analysis(provider, username, repo)
