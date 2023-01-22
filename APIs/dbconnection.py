import pymysql

conncmd=""
def init():
    with open('./apis/dbcommand.dbinfo',"r") as f:    
        conncmd = f.read()    
    print(conncmd)

def getConnection():
    conn=None
    exec("conn="+conncmd)
    return conn

init()
'''
sql = "insert into user(username,password) values(%s,%s)"
rows = cursor.excute(sql,('jason','123'))
'''