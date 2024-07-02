import requests

# Aternos login details
USERNAME = 'IRFRunner'
PASSWORD = 'IRFRunner123'
SERVER_ID = '0q07R1ZoC9NykApbRol7'

def login():
    session = requests.Session()
    login_url = 'https://aternos.org/panel/ajax/account/login.php'
    login_data = {
        'user': USERNAME,
        'password': PASSWORD
    }
    response = session.post(login_url, data=login_data)
    return session

def start_server(session):
    start_url = f'https://aternos.org/panel/ajax/start.php?SERIAL={SERVER_ID}'
    response = session.get(start_url)
    return response.status_code

def main():
    session = login()
    if session:
        status_code = start_server(session)
        if status_code == 200:
            print('Server is starting...')
        else:
            print('Failed to start the server.')

if __name__ == '__main__':
    main()
