# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 07:47:42 2020

@author: Eshika Mahajan
"""

from urllib.request import urlopen 

android_url="https://en.wikipedia.org/wiki/Android_version_history"
#URL that we want to open
android_data=urlopen(android_url) #requesting to open this URL
print(type(android_data))

android_html=android_data.read()  #reading the html file of the url
#print(android_html)
android_data.close() #closing the html doc after reading

#-----------------------PARSING DATA------------------------------
from bs4 import BeautifulSoup as soup
android_soup=soup(android_html,'html.parser') #initialising the soup with the document we want to read and the type of document we want to parse
print(android_soup)

print(android_soup.h1)  #prints the tag of first heading
android_soup.h1   #gives the same output as above

android_soup.findAll('h1',{})
#the above function returns the list of all the headings with h1 tag . we also pass anempty dictionary as the second argument
tables=android_soup.findAll('table',{'class':'wikitable'})
print(len(tables))
android_table=tables[0]
print(tables[0])


#getting the headings of the table column
headers=android_table.findAll('th')
print(len(headers))
headers[0].text

column_title=[ct.text[:] for ct in headers]   #fetching all the column titles with a \n with their names

#getting rows of the data excluding the first heading row
rows_data=android_table.findAll('tr')[1:]
first_row=rows_data[0]

#printing the data in first row with <td> tag
first_row=rows_data[0].findAll('td',{})
for data in first_row:
    print(data.text)
    
#similarly getting data from all the rows
table_rows=[]

for row in rows_data:
    current_row=[]
    row_data=row.findAll('td',{})
    for idx,data in enumerate(row_data):
        current_row.append(data.text[:-1]) #to remove \n
    table_rows.append(current_row)
    
#SAVING THE TABLE IN A CSV FILE


file='parsing_table.csv'
with open(file,'w',encoding='utf-8') as f:
    header_string=','.join(column_title)
    header_string+='\n'
    f.write(header_string)
    
    for row in table_rows:
        row_string=""
        row_string=','.join(row)
        row_string+='\n'
        f.write(row_string)
    