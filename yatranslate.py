import requests



URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_some(key, in_word, from_lang, to_lang='ru'):
    params = {
        'key': key,
        'text': in_word,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    result = []
    try:
        json_ = response.json()
        #print('Response code:', response.status_code)
        if response.status_code == 200:
            result = [response.status_code, ''.join(json_['text'])]
        elif response.status_code == 403:
            result = [response.status_code]
    except ConnectionError as ce:
        print(ce)
        #print('Response code:', result[0])
    if len(result) > 1:
        print('Translate is:', result[1])
    return result

if __name__ == '__main__':
    API_KEY = input('Введите ключ API_KEY к сервису Yandex-translate: ')
    new_res = translate_some(API_KEY, 'hello','en','ru')
    if len(new_res) > 1:
        print('Translate result is: ', new_res[1], '; Response code:', new_res[0])
    else:
        print('Some error found')
