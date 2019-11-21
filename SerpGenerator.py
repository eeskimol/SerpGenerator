#! /usr/bin/env python
# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup as bts
import urllib
import random
import copy
import codecs
from sys import argv

def BaseGet():
    pass

def PageGet(url):
    pass


class Serp:
    def __init__(self,SoupPage):
        self.serp = bts(SoupPage,'lxml')

    def DelGuide(self):
        dup=self.serp
        #for i in range(3,10):
        for i in range(1,10):
            bar = dup.find(attrs={'aria-label':'Page '+str(i)})
            if bar is not None:
                bar.extract()
            
        pass

     

    def DelBar(self):
        dup = self.serp
        bar = dup.find(attrs={'id':'b_context'})
        if bar is not None:
            bar.extract()
    def DelQuest(self):
        dup = self.serp
        quest = dup.find(attrs={'class':'b_mt','id':'cvnMt'})
        if quest is not None:
                           quest.extract()
        pass

    def PageRand(self):
        dup = self.serp
        results = dup.find(attrs={'id':'b_results'})
        org = results.find_all(attrs={'class':'b_algo'})
        blist = []
        for i in org:
            blist.append(copy.copy(i))

        aaa='''
        random.shuffle(blist)
        for i in range(0,len(org)):
            org[i].replace_with(blist[i])
              #  print results.contents[i]['id']
        with codecs.open('newb.html','w',encoding='utf-8') as f:
            f.write(unicode(dup)) 
            '''
        return [blist,org]
    def Record(self,fname):
        with codecs.open(fname,'w',encoding='utf-8') as f:
            f.write(unicode(self.serp))
                
def InterRand(flist,slist):
    mlist = flist[0] + slist[0]  
    random.shuffle(mlist)
    for i in range(0,len(flist[1])):
        flist[1][i].replace_with(mlist[i])
    for i in range(0,len(slist[1])):
        slist[1][i].replace_with(mlist[i+len(flist[1])])

def main(name,mode):
    with open(name+'.html','r') as doc:
        page1 = doc.read()
    aches = Serp(page1)
    aches.DelBar()
    aches.DelGuide() 
        
    if  1&int(mode)== 0 :# without question ,1x refers to good serp ;0x refers to bad serp
        aches.DelQuest()
    else : #with question
        pass

    aches.Record(name+'-'+mode+'.html')



if __name__ == '__main__':
    name,mode = argv
    main(name,mode)

