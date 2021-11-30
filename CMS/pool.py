import pymysql as MYSQL
def ConnectionPooling():
    db=MYSQL.connect(host="localhost",port=3306,user="root",password="Nivesh@1234",db="cms")
    cmd=db.cursor()
    return db,cmd