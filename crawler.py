import requests
import bs4

def getlinks(url):

  resp=requests.get(url)  
  soup=bs4.BeautifulSoup(resp.content,features="html.parser")
  title = soup.find_all("title")
  links = soup.find_all("a", attrs ={"class":"title"} )
  for i in links:
    print(i['href'])
   
if __name__ == "__main__" :  
  main()
  
