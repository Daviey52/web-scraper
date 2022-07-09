
from sys import prefix
import requests , openpyxl
from bs4 import BeautifulSoup

def  get_citations_needed_count(URL):
  page = requests.get(URL)
  soup = BeautifulSoup(page.content,'html.parser')
  results = soup.find_all(class_="noprint Inline-Template Template-Fact")
  print (len(results))
  return len(results)
get_citations_needed_count(URL='https://en.wikipedia.org/wiki/Gene_therapy')

def get_citations_needed_report(URL):
  page = requests.get(URL)
  contents = page.content
  soup = BeautifulSoup(page.content,'html.parser')
  results = soup.find_all(class_="noprint Inline-Template Template-Fact")
  res = ''
  prefix = 'Citation needed for :'

  for result in results:
    parents = result.find_parents('p')
    for parent in parents:
      res += prefix + parent.text + '\n'
      print(res)
get_citations_needed_report(URL='https://en.wikipedia.org/wiki/Gene_therapy')


