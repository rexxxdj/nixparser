# -*- coding: utf-8 -*-
import requests
import csv
from lxml import html
import json

class ycombinatorParser():
    siteurl = 'https://news.ycombinator.com/'    

    def getNextPage(pageurl):
        response = requests.get(pageurl)
        parsed_body = html.fromstring(response.text)
        nextpage=parsed_body.xpath('//a[@class="morelink"]')
        try:
            nexthref=nextpage[0].get('href')
        except IndexError:
            nexthref = ''
        return nexthref  


    def parsePage(parsed_body,rownumber):
        def jsonWriteLine(rownumber,title,autor,url,site):
            line = '{"Rownumber": %d,\n "title": "%s",\n "autor": "%s",\n "url": "%s",\n "site": "%s",\n }\n' %(rownumber,title,autor,url,site)
            #print line
            return line

        def getNews(rownews):
            newsdict = {}
            for news in rownews:
                newsdict["title"] = ''.join(news.xpath('./a/text()'))
            for i in news.xpath('./a'):
                newsdict["url"] = i.get('href')
                newsdict["site"] = ''.join(news.xpath('./span/a/span/text()'))
            return newsdict

        def getAuthor(rowautor):
            authordict = {}
            for author in rowautor:
                authordict["autor"] = ''.join(author.xpath('./a[1]/text()'))
            return authordict

        for row in parsed_body.xpath('//tr'):
            rownews = row.xpath('./td[@class="title"][2]')
            rowautor = row.xpath('./td[@class="subtext"][1]')
            datadict = {}
            rowdata = {}
            if rownews:
                datadict = getNews(rownews)
            if rowautor:
                for author in rowautor:
                    datadict = getAuthor(rowautor)

            if datadict:
                autor = ''
                try:
                    title=datadict["title"]
                    url=datadict["url"]
                    site=datadict["site"]
                except KeyError:
                    autor = datadict["autor"]

                if autor:
                    rowdata['rownumber'] = str(rownumber)
                    rowdata['title'] = str(title)
                    rowdata['autor'] = str(autor)
                    rowdata['url'] = str(url)
                    rowdata['site'] = str(site)
                    
                    with open('nix.json',mode='a') as f:
                        json.dump(rowdata,f)
                    
                    #outputfile.write(jsonWriteLine(rownumber,title,autor,url,site))     
                    
                    #print jsonWriteLine(rownumber,title,autor,url,site)
                    rownumber += 1
                    if rownumber>2:
                        exit()
        return rownumber
    
        def __unicode__(self):
            return unicode(self.rowdata)
    
    pageflag = True
    rownumber = 1
    pageparse = siteurl
    with open('nix.json',mode='w') as f:
        json.dump('',f)
    while pageflag:        
        response = requests.get(pageparse)
        parsed_body = html.fromstring(response.text)       

        rownumber = parsePage(parsed_body,rownumber)-1

        pageparse = siteurl+getNextPage(pageparse)
        if pageparse == siteurl:
            pageflag = False
if __name__ == '__main__':
    ycombinatorParser()