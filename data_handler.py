import database_common
from psycopg2 import IntegrityError


@database_common.connection_handler
def add_new_user(cursor, user_name, password ):
    try:
        cursor.execute("""
                        INSERT INTO users (user_name, password) 
                        VALUES (%(user_name)s, %(password)s )
                        """,
                       {
                           "user_name": user_name,
                           "password": password
                           })

        cursor.execute("""
                        SELECT MAX(user_id) AS created_id 
                        FROM users
                        """)

        new_id = cursor.fetchall()
    except IntegrityError as error:
        return "Error: " + str(error), -1

    return "Registration Successful", new_id


@database_common.connection_handler
def get_user_and_password(cursor, user_name):
    try:
        cursor.execute("""
                        SELECT user_name, password, user_id FROM users
                        WHERE user_name = %(user_name)s
                        """,
                       {'user_name': user_name})
        login_data = cursor.fetchone()
    except TypeError:
        return "error: Type error", -1
    return login_data
