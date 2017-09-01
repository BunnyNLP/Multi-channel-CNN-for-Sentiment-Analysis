#!/usr/local/lib
# -*-coding:utf-8-*-
import csv
import pymysql
import re
aPath='/home/jamie/Reserch/Test.csv'
bPath='/home/jamie/Reserch/result_bs.csv'
sen = {}
v = {}
sem = {}
def index(aPath,bPath):
    aFile = open(aPath, 'r')#因为这个文件是以空格分行，所以要这这样写
    aInfo = csv.reader(aFile)
    for info in aInfo:
        id,sentence = info[0].split('\t')
        sen[id]= sentence.replace('"','\t')\
                         .replace("'","\t")\
                         .replace("👉","\t")\
                         .replace("/","\t")\
                         .replace("<","\t")\
                         .replace("👈","\t")\
                         .replace("👯","\t")\
    #print(a)


    bFile = open(bPath, 'r')
    bInfo = csv.reader(bFile)
    for id,view,semtiment in bInfo:
        v[id]= view
        sem[id]= semtiment
    #print(v)



#处理数据库的函数
def mysql_database():
    db = pymysql.connect(host='localhost',user='root',passwd='aptx4869',db='Results',charset='utf8')

    dbc = db.cursor()
    dbc.execute('SET NAMES utf8;') 
    dbc.execute('SET CHARACTER SET utf8;')
    dbc.execute('SET character_set_connection=utf8;')
    #max_steps = 31225
    for id,view in v.items():
        process_bar.show_process()
        #time.sleep(0.05)
        #print(type(sen[id]))
        idt=int(id)
        #print(idt)
        sql = '''INSERT INTO test(id,semtiment,view,sentence) VALUES(%i,"%s","%s","%s")''' %(idt,sem[id],v[id],sen[id])
        dbc.execute(sql)
    process_bar.close()
    '''
    id='111551'
    idt=int(id)
    
    print(sql)
    dbc.execute(sql)
    '''


    db.commit()
    #cursor.close()
    db.close()
    #print('同步数据库成功！')



#进度条
import sys, time
class ShowProcess():
    """
    显示处理进度的类
    调用该类相关函数即可实现处理进度的显示
    """
    i = 0 # 当前的处理进度
    #max_steps = 31225 # 总共需要处理的次数
    max_arrow = 50 #进度条的长度

    # 初始化函数，需要知道总共的处理次数
    def __init__(self, max_steps):
        self.max_steps = max_steps
        self.i = 0

    # 显示函数，根据当前的处理进度i显示进度
    # 效果为[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
    def show_process(self, i=None):
        if i is not None:
            self.i = i
        num_arrow = int(self.i * self.max_arrow / self.max_steps) #计算显示多少个'>'
        num_line = self.max_arrow - num_arrow #计算显示多少个'-'
        percent = self.i * 100.0 / self.max_steps #计算完成进度，格式为xx.xx%
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r' #带输出的字符串，'\r'表示不换行回到最左边
        sys.stdout.write(process_bar) #这两句打印字符到终端
        sys.stdout.flush()
        self.i += 1

    def close(self, words='done'):
        print ('')
        print (words)
        self.i = 1

if __name__=='__main__':
    index(aPath,bPath)
    #print(v)
    
    max_steps = len(v)
    process_bar = ShowProcess(max_steps)

    mysql_database()
    '''
    for i in range(max_steps + 1):
        process_bar.show_process()
        #time.sleep(0.05)
    process_bar.close()
    '''

