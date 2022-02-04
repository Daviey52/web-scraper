
import requests
from bs4 import BeautifulSoup

def  get_citations_needed_count(URL):
  page = requests.get(URL)
  soup = BeautifulSoup(page.content,'html.parser')
  results = soup.find_all(class_="noprint Inline-Template Template-Fact")
  return len(results)
get_citations_needed_count(URL='https://en.wikipedia.org/wiki/Gene_therapy')

def get_citations_needed_report(URL):
  page = requests.get(URL)
  contents = page.content
  soup = BeautifulSoup(page.content,'html.parser')
  #results = soup.find_all(class_="noprint Inline-Template Template-Fact")
  results2 = soup.find_all(class_="noprint Inline-Template Template-Fact")
  results = soup.find_all('p')

  if results2 and results != ('sup id'):
    for result in results:
      print(result)


get_citations_needed_report(URL='https://en.wikipedia.org/wiki/Gene_therapy')


