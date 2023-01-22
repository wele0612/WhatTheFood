import csv
import re
 
filename='grocery_class.csv'
data = []

def standardlize(name:str):
    name=name.lower()
    name=re.sub(r'[0-9]+', '', name)
    return name

def init():
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        #header = next(csv_reader)        # 读取第一行每一列的标题
        for row in csv_reader:            # 将csv 文件中的数据保存到data中
            data.append({'name':standardlize(row[0]),'class':row[1]});           # 选择某一列加入到data数组中

def getClass(name:str):
        name=standardlize(name)
        for item in data:
            if name.count(item['name'])>0:
                 return {'name':item['name'],'class':item['class']}
        return None

init()
r=getClass("BaNA12na")
print(r)