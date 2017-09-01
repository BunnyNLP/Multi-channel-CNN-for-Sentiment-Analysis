#!/usr/bin/env
#coding:utf-8
from whoosh.fields import *
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import os.path
import whoosh
from whoosh.analysis import RegexAnalyzer
import csv

from whoosh import qparser
analyzer = RegexAnalyzer(r'([\u4e00-\u9fa5])|(\w+(\.?\w+)*)')#中文语法分析器

def createIndexs(dirName):
    schema = Schema(id=NUMERIC(sortable=True),views=KEYWORD(stored=True), semtiment=TEXT(stored=True),content=TEXT(stored=True,analyzer=analyzer))

    if not os.path.exists(dirName):
        os.mkdir(dirName)
    ix = create_in(dirName, schema)
    dic={}
    for line in open('Test.csv'):
        id,content=line.split('\t')
        dic[id]=content
    writer = ix.writer()
    reader=csv.reader(open('result_bs.csv'))
    for id,view,sem in reader:
        writer.add_document(id=id,views=view,semtiment=sem,content=dic[id])
    p = writer.commit()

'''
    writer.add_document(id=100000,views=u"大众",semtiment=u"pos",content=u"This is my first sentences!This is my first !I am 大众!!!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!")
    writer.add_document(id=100000,views=u"大众",semtiment=u"neu",content=u"This is my first sentences!This is my first !I am 大众!!!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!This is my first sentences!")
    writer.add_document(id=100001,views=u"奔驰",semtiment=u"pos",content=u"This is my second sentences!")
    writer.add_document(id=100002,views=u"QQ",semtiment=u"neu",content=u"This is my third sentences!")
    writer.add_document(id=100003,views=u"大黄蜂",semtiment=u"pos",content=u"This is my fourth sentences!")
'''
    

def query(dirName,key,rank):
    ix = open_dir(dirName)#第一步:若索引已添加了，调用open_dir("dir of index")即可返回index,若出现exception则说明，还没有添加任何索引。
    with ix.searcher() as searcher:
        '''
        通过调用index.searcher(),根据index生成searcher. searcher就是打开的一堆文件，用完一定要关闭。 searcher有很多获取索引信息的有用方法，
    比如lexicon(fieldname):得到某字段的全部分词。当然其中最重要的方法就是search方法。
        '''

         #生成查询对象,类似于：myquery = And([Term("content", u"apple"), Term("content", "bear")])
        user_q=qparser.QueryParser("content", ix.schema).parse(key)

        '''
        # Only show documents in the "rendering" chapter
        allow_q = query.Term("semtiment", "pos")
        # Don't show any documents where the "tag" field contains "todo"
        restrict_q = query.Term("tag", "todo")
        results = s.search(user_q, filter=allow_q, mask=restrict_q)
        '''
        #过滤器
        #allow_q=query.Term("semtiment","pos")
        #restrict_q=query.Term("semtiment","neu")
        #allow_q =QueryParser("semtiment", ix.schema).parse(rank)

	
        
        #results = searcher.search(user_q,filter=allow_q,mask=restrict_q,limit=1,terms=True)#以query对象为参数调用searcher的search方法.得到查询result.
	results = searcher.search(user_q,filter=allow_q,limit=1,terms=True)#以query对象为参数调用searcher的search方法.得到查询result.
        results= searcher.search_page(query,pagenum=1, pagelen=1000000)#The default page length is 10 hits. You can use the pagelen keyword argument to set a different page length:
        print('<h1>一共有',len(results),'条结果</h1>\n')
        for hit in results:
            print(hit['views'],hit['semtiment'])
            print('</br>')
            #print(hit['content'])
        # Assume "content" field is stored
            print(hit.highlights("content")+'</br>'+'<hr>')
            #print (whoosh.highlight.SentenceFragmenter("content"))
            #print(results)
            #print(hit)
            #print (results.matched_terms())
            #print(hit.matched_terms())
            

        my_cf = whoosh.highlight.ContextFragmenter(maxchars=100, surround=30)
        results.fragmenter = my_cf
        return {"total":len(results)}




if __name__ == '__main__':
 
    #createIndexs("indexDir")
    rt =query("indexDir",'大众','neu')
    print(rt)


