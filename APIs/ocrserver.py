from flask import Flask,request,make_response
import json
import pymysql
import dbconnection as db
import paddlehub as hub
import cv2
import base64
import numpy as np
from flask_cors import cross_origin
import grocery

app = Flask(__name__)
ocr = hub.Module(name="chinese_ocr_db_crnn_mobile", enable_mkldnn=True) 
grocery.init()
db.init()
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

@app.route('/')
def hello_world():
    return 'OCR server running.'

@app.route('/api/ocr',methods=['POST'])
@cross_origin()
def ocrImage():
 
    file = request.form.get('imgData')
    data_url = str.split(file, ',')[1]

    img_data = base64.urlsafe_b64decode(data_url + '=' * (4 - len(data_url) % 4))
    img_data = np.frombuffer(img_data, np.uint8)
    img_data=cv2.imdecode(img_data, cv2.IMREAD_COLOR)
    #print(img_data)
    #cv2.imwrite('img1.jpg', img_data)

    result = ocr.recognize_text(images=[img_data])
    textLines=result[0]["data"]
    ocrtextList=[]
    for line in textLines:
        ocrtextList.append(line["text"])

    '''outfile=open('result.json', mode = 'w',encoding='utf-8')
    finaljson=json.dumps(ocrtextList)
    print(finaljson,file=outfile)
    outfile.close
    '''
    #print(result,file=outfile)

    classlist=[]
    for item in ocrtextList:
        c=grocery.getClass(item)
        if c['name']!="":
            if not c==None:
                classlist.append(c)


    print("Done.")

    return json.dumps({'code':0,'ocr_result':classlist})

@app.route('/api/repository',methods=['POST'])
@cross_origin()
def updateRepository():
    return "Funciton not complete"

@app.route('/api/login',methods=["POST"])
@cross_origin()
def login():
    user = request.form['user']
    password = request.form['password']
    conn=db.getConnection()
    cursor=conn.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT * FROM users where username=%s and password=%s"
    rows = cursor.execute(sql,(user,password))
    if rows==1:
        resp = make_response("success")
        resp.set_cookie("SESSDATA", user,max_age=36000)
    elif cursor.execute("SELECT * FROM users where username=%s",(user)):
        resp = make_response("wrong password")
    else:
        resp = make_response("created")

    conn.close()
    return resp


def checkAuth(sessdata:str):
    return "userName"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

