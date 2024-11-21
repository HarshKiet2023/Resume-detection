import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='yuvi@007',
        db='cv'
    )
    print("Connection to MySQL database successful!")
except Exception as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    if connection:
        connection.close()
