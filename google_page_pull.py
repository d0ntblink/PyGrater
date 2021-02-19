from bs4 import BeautifulSoup
from random import randrange
import requests
from requests.api import get

A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )

def create_url():
    search_string = input("What is your question ? ")
    url = search_string.replace(' ', '+')
    url = 'https://google.com/search?q=' + url
    return url


def get_html(url):
    user_agent = A[randrange(len(A))]
    headers = {'user-agent': user_agent}
    html_content = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_content, "lxml")
    return soup


# Call the Functions
url = create_url()
soup = get_html(url)

# Find the answer
answer = soup.find("div", class_="BNeawe iBp4i AP7Wnd")

#Clean The Answer and Create Conditon for No Answer
if answer == None:
  print("Suprise! Google does not know the answer to that question!")
else:
  print(answer.text)
