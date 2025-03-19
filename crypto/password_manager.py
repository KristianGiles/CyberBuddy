import psycopg2
from psycopg2.extras import RealDictCursor
import getpass

def get_creds():
    username = input('Username: ')
    password = getpass.getpass('Password: ')

    return username, password
def try_connect(username, password):
    try:
        connection = psycopg2.connect(
            database='postgres',
            user=f'{username}',
            password=f'{password}',
            host='user.cxwisogg8h4s.ap-southeast-2.rds.amazonaws.com',
            port='5432'
        )
        print('Connection Successful.')

        return connection
    except Exception as e:
        print(e)
        print('Connection Failed.')
        return True
