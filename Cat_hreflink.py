#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Используемые внешние библиотеки

import requests
from bs4 import BeautifulSoup
import time


#Получение первичных ссылок

class Cat_hreflink ():    
    
    
    def __init__ (self, parse_cat_links, classlinks):
        
        self.parse_cat_links = str(parse_cat_links)
        self.classlinks = str(classlinks)
        self.links = []
        self.allhrefs = [] #сюда складываем ссылки из линкграббера
        self.length = 0
        
        
    def linkgrabber (self):
        
        print ('')
        print ('Cat_hreflink. Парсер ссылок по локаторам-классам')
        print ('Версия программы - 1.0')
        print ('Последнее обновление - 08.05.2019')
        print ('IMVO.SITE')
        print ('')
        
        
        r = requests.get(self.parse_cat_links)
        soup = BeautifulSoup(r.text, 'html.parser')
        self.links = soup.find(  ).find_all( class_= self.classlinks )    
        
        print ('Ждите. Собираем ссылки')
        
        for href in self.links:
            href = href['href']
            self.allhrefs.append(href)
            time.sleep(0.5)
            
        print ('Сбор ссылок завершен. Получить данные - allhrefs, узнать количество ссылок - length')

        self.length = len(self.allhrefs)
        
        
#Обработка ссылок

        
class Urlconstructor:
    def __init__ (self, url, allhrefs):
        self.url = url
        self.allhrefs = allhrefs
        self.links = []
        
    def urlconstructor (self):
        
        for x in self.allhrefs:
            x = self.url + x
            self.links += [x]
        print ('')  
        print ('Обработка ссылок завершена. Забрать ссылки - links')

