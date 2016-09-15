import requests
import io
import os.path
from bs4 import BeautifulSoup
url="http://www.imdb.com/chart/top?ref_=nv_mv_250_6"
r = requests.get(url)
bs = BeautifulSoup(r.text)
save_path="F:/"
completeName=os.path.join(save_path,"output.txt")
g_data = bs.find_all("tbody",{"class":"lister-list"})
rank=0
for movie in g_data:
    for trmovie in movie.find_all("tr"):
        rank=rank+1
        title= trmovie.find("td","titleColumn").contents[1].text
        rating= trmovie.find("td","ratingColumn").contents[1].text
        print rank,title,rating
        
        
