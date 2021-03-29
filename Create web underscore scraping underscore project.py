In [ ]:
#Requirements
#pip3 install requests
#pip3 install bs4
Basic fundamentals of web scraping
In [49]:
# import these two modules bs4 for selecting HTML tags easily
from bs4 import BeautifulSoup
# requests module is easy to operate some people use urllib but I prefer this one because it is easy to use.
import requests

# I put here my own blog url ,you can change it.
url="https://getpython.wordpress.com/"

#Requests module use to data from given url
source=requests.get(url)

# BeautifulSoup is used for getting HTML structure from requests response.(craete your soup)
soup=BeautifulSoup(source.text,'html')

# Find function is used to find a single element if there are more than once it always returns the first element.
title=soup.find('title') # place your html tagg in parentheses that you want to find from html.
print("this is with html tags :",title)

qwery=soup.find('h1') # here i find first h1 tagg in my website using find operation.

#use .text for extract only text without any html tags
print("this is without html tags:",qwery.text) 


links=soup.find('a') #i extarcted link using "a" tag
print(links)
this is with html tags : <title>Easy Python – A programming language of revolution</title>
this is without html tags: Easy Python
<a class="screen-reader-text skip-link" href="#content">Skip to content</a>
extarct data from innerhtml
In [41]:
# here i extarcted href data from anchor tag.
print(links['href'])
#content
In [42]:
# similarly i got class details from a anchor tag
print(links['class'])
['screen-reader-text', 'skip-link']
findall operation in Bs4
In [51]:
# findall function is used to fetch all tags at a single time.
many_link=soup.find_all('a') # here i extracted all the anchor tags of my website
total_links=len(many_link) # len function is use to calculate length of your array
print("total links in my website :",total_links)
print()
for i in many_link[:6]: # here i use slicing to fetch only first 6 links from rest of them.
    print(i)
total links in my website : 37

<a class="screen-reader-text skip-link" href="#content">Skip to content</a>
<a href="https://getpython.wordpress.com/" rel="home">
<div class="cover"></div>
</a>
<a class="screen-reader-text search-toggle" href="#search-container">Search</a>
<a href="https://getpython.wordpress.com/" rel="home">Easy Python</a>
<a aria-current="page" href="/">Home</a>
<a href="https://getpython.wordpress.com/contact/">Contact</a>
In [54]:
second_link=many_link[1] #here i fetch second link which place on 1 index number in many_links.
print(second_link)
print()
print("href is :",second_link['href']) #only href link is extracted from ancor tag
<a href="https://getpython.wordpress.com/" rel="home">
<div class="cover"></div>
</a>

href is : https://getpython.wordpress.com/
In [59]:
# select div tag from second link
nested_div=second_link.find('div')
# As you can see div element extarcted , it also have inner elements
print(nested_div)
print()
#here i extracted class element from div but it give us in the form of list
z=(nested_div['class'])
print(z)
print(type(z))
print()
#  " " .join () method use to convert list type  into string type
print("class name of div is :"," ".join(nested_div['class']))
<div class="cover"></div>

['cover']
<class 'list'>

class name of div is : cover
scrap data from wikipedia
In [60]:
wiki=requests.get("https://en.wikipedia.org/wiki/World_War_II")
soup=BeautifulSoup(wiki.text,'html')
print(soup.find('title'))
<title>World War II - Wikipedia</title>
find html tags with classes
In [65]:
ww2_contents=soup.find_all("div",class_='toc')
for i in ww2_contents:
    print(i.text)
Contents

1 Chronology
2 Background

2.1 Europe
2.2 Asia


3 Pre-war events

3.1 Italian invasion of Ethiopia (1935)
3.2 Spanish Civil War (1936–1939)
3.3 Japanese invasion of China (1937)
3.4 Soviet–Japanese border conflicts
3.5 European occupations and agreements


4 Course of the war

4.1 War breaks out in Europe (1939–40)
4.2 Western Europe (1940–41)
4.3 Mediterranean (1940–41)
4.4 Axis attack on the Soviet Union (1941)
4.5 War breaks out in the Pacific (1941)
4.6 Axis advance stalls (1942–43)

4.6.1 Pacific (1942–43)
4.6.2 Eastern Front (1942–43)
4.6.3 Western Europe/Atlantic and Mediterranean (1942–43)


4.7 Allies gain momentum (1943–44)
4.8 Allies close in (1944)
4.9 Axis collapse, Allied victory (1944–45)


5 Aftermath
6 Impact

6.1 Casualties and war crimes
6.2 Genocide, concentration camps, and slave labour
6.3 Occupation
6.4 Home fronts and production
6.5 Advances in technology and warfare


7 See also
8 Notes
9 Citations
10 References
11 External links


In [68]:
overview=soup.find_all('table',class_='infobox vevent')
for z in overview:
    print(z.text)
World War II(clockwise from top left)
Chinese forces in the Battle of Wanjialing
Australian 25-pounder guns during the First Battle of El Alamein
German Stuka dive bombers on the Eastern Front in December 1943
American naval force in the Lingayen Gulf
Wilhelm Keitel signing the German Instrument of Surrender
Soviet troops in the Battle of Stalingrad
Date1 September 1939 – 2 September 1945 (1939-09-01 – 1945-09-02)(6 years and 1 day)[a]LocationEurope, Pacific, Atlantic, South-East Asia, China, Middle East, Mediterranean, North Africa, Horn of Africa, Australia, briefly North and South AmericaResult
Allied victory
Collapse of Nazi Germany
Fall of the Japanese and Italian Empires
Beginning of the Nuclear Age
Dissolution of the League of Nations
Creation of the United Nations
Emergence of the United States and the Soviet Union as rival superpowers
Beginning of the Cold War (more...)Participants
Allies
AxisCommanders and leaders
Main Allied leaders
 Joseph Stalin
 Franklin D. Roosevelt
 Winston Churchill
 Chiang Kai-shek

Main Axis leaders
 Adolf Hitler
 Hirohito
 Benito Mussolini
Casualties and losses

Military dead:
Over 16,000,000
Civilian dead:
Over 45,000,000
Total dead:
Over 61,000,000
(1937–1945)
...further details


Military dead:
Over 8,000,000
Civilian dead:
Over 4,000,000
Total dead:
Over 12,000,000
(1937–1945)
...further details
