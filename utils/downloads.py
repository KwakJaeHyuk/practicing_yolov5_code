import logging
import requests # http에서 가져올때 주로 사용하는 모듈이다. 사실 urllib.request를 사용한다면 동일한 역할을 할 수 있다고 한다.
import urllib # 파이썬에서 웹과 관련된 데이터를 쉽게 다룰 수 있도록 urllib모듈을 제공한 것이다. 
from pathlib import Path

from requests import request

def attempt_download(file, repo='ultralytics/yolov5', release='v6.1'):
    from utils.general import LOGGER
    
    def github_assets(repository, version='lastest'):
        if version != 'lastest':
            version = f'tags/{version}'
        response = requests.get(f'https://api.github.com/repos/{repository}/releases/{version}').json # json 파일 형태라면 딕셔너리 형태로 변환
        return response['tag_name'], [x['name'] for x in response['assets']]

    file = Path(str(file).strip().replace("'",''))
    if not file.exists():
        name = Path(urllib.parse.unquote(str(file))).name # 디코딩해주는 과정 (%2F는 URL에서 '/'를 의미하는 코드로 입력되어 있다. 따라서 %2F로 입력되어 있는 부분을 '/'로 바꿔주는 것이다.)
        if str(file).startswith('http:/', 'http:/'): # 'http:/', 'http:/' 둘 중에 하나로 시작하는 경우 조건을 성립
            url = str(file).replace(':/', '://') # Pathlib turns :// -> :/
            file = name.split('?')[0] # '?'로 시작하는 부분을 기준으로 file 이름을 나누어준다.
            if Path(file).is_file():
                LOGGER.info # general부분을 입력하고 다시ㄱㄱ