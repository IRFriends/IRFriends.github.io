import requests
import os

# Aternos login details from environment variables
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
SERVER_ID = os.getenv('SERVER_ID')

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
