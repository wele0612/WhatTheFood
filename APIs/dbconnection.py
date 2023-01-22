import pymysql

dbpassword=""
def init():
    with open('./apis/dbcommand.dbinfo',"r") as f:    
        dbpassword = f.read()    
    print("dbpassword: "+dbpassword)

def getConnection():
    with open('./apis/dbcommand.dbinfo',"r") as f:    
        dbpassword = f.read()
    #print("password:"+dbpassword)
    conn=pymysql.connect(host= '127.0.0.1', port=3306, user= 'root', password= dbpassword, db= 'grocery', charset = 'utf8', autocommit = True)
    return conn

init()
'''
sql = "insert into user(username,password) values(%s,%s)"
rows = cursor.excute(sql,('jason','123'))
'''