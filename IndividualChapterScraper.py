import requests
from bs4 import BeautifulSoup
current = "https://parahumans.wordpress.com/2013/11/16/teneral-e-5/"
worm = requests.get(current)
arc = worm.content
soup = BeautifulSoup(arc, "lxml")
text = soup.get_text()
start = text.index("Next Chapter")
end1 = text.index("Next Chapter")
end = text.index("Next Chapter", end1 + 1)
chapter = text[start:end]
chapter = chapter.encode('utf-8',errors='ignore')
current = current.encode('utf-8',errors='ignore')
print(chapter)
file = open("Teneral5.txt","a") 
file.write(current)
file.write(chapter)
file.close
