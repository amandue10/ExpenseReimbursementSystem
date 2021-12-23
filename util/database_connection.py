import os

from psycopg2 import connect, OperationalError


# from psycopg import connect, OperationalError


def create_connection():
    try:
        conn = connect(
            host=os.environ.get("HOST"),
            database=os.environ.get("DB"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        return conn
    except OperationalError as e:
        print(str(e))


connection = create_connection()

print(connection)
#     try:
#         conn = connect(
#             host=os.environ.get("HOST"),
#             dbname=os.environ.get("DB"),
#             user=os.environ.get("USER"),
#             password=os.environ.get("PASSWORD"),
#             port=os.environ.get("PORT")
#         )
#         return conn
#     except OperationalError as e:
#         print(str(e))
#
#
# connection = create_connection()
#
# print(connection)
