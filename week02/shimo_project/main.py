from fake_useragent import UserAgent
import requests
import json

home_page = 'https://shimo.im'
login_page = 'https://shimo.im/lizard-api/auth/password/login'
user_api_page = 'https://shimo.im/lizard-api/users/me'

user_agent = {'User-Agent': UserAgent(verify_ssl=False).random}
login_header = {
    'referer': 'https://shimo.im/login?from=home',
    'x-requested-with': 'XmlHttpRequest',
}
api_headers = {
    'referer': 'https://shimo.im/dashboard',
}


def login(session):
    with open('param.json', 'r') as fin:
        form_data = json.load(fin)
    r = session.post(login_page, data=form_data, headers=login_header)
    # print(r.status_code)
    return r.raise_for_status()


def get_user_data(session):
    r = session.get(user_api_page, headers=api_headers)

    try:
        r.raise_for_status()
    except requests.HTTPError as e:
        raise e

    return r.text


def main():
    with requests.session() as s:
        s.headers.update(user_agent)
        s.get(home_page)

        try:
            login(s)
            data = get_user_data(s)
        except requests.HTTPError as e:
            print(e)
            return

    with open('user_data.json', 'w', encoding='utf-8') as fout:
        fout.write(data)


if __name__ == "__main__":
    main()
