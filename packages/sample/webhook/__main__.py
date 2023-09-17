import os
import psycopg2

db_host = str(os.getenv('DB_HOST'))
db_name = str(os.getenv('DB_NAME'))
db_user = str(os.getenv('DB_USER'))
db_pass = str(os.getenv('DB_PASS'))
db_port = str(os.getenv('DB_PORT'))


def main(args):
    greeting = "Farewell " + db_name + "!" + db_user + db_port + db_name + db_host
    print(greeting)
    return {"body": greeting}


def db_connect():

    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(dbname=db_name,
                                host=db_host,
                                user=db_user,
                                password=db_pass,
                                port=db_port,
                                sslmode='require',
                                sslrootcert='file/ca-certificate-4care-2.crt')

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        message = 'postgreSQL version:' + db_version

        # close the communication with the PostgreSQL
        cur.close()
        return conn, message

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return conn, error


def get_env_value():
    print(db_host)
    print(db_name)
    print(db_user)
    print(db_port)
    message = db_host + db_name + db_user + db_port
    print(message)
    return None, message

