import MySQLdb

def mysql_connect():
    connection=MySQLdb.connect(
        password="NlXCS1Tk6ilqKBc9gEvm",
        database="railway", 
        user="root", 
        port=5920,
        host="containers-us-west-172.railway.app",
        charset='utf8mb4'
    )
    return connection