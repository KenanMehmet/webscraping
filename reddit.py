from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re

session = HTMLSession()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'

def GamesNews():
    output = ""
    request = session.get("https://old.reddit.com/r/Games/comments/12qo0ih/dead_island_2_review_thread/", headers={'User-Agent': user_agent})
    #print(request.html.find('div#thing_t3_12o1yrg', first=True).text)
    #print(body.text)
    soup = BeautifulSoup(request.text, 'html.parser')
    body = soup.find('div', {"class": "entry unvoted"})
    p_tag = body.find('strong', string=re.compile("Game Title"))
    output += p_tag.parent.text +"\n"
    #output += soup.find('p', string=re.compile("Game Title")).text
    open_critic = body.find('a', string=re.compile("OpenCritic"))
    output += open_critic.text +"\n"
    ign = body.find('strong', string=re.compile("IGN"))
    
    print(ign.parent.text)
    print(ign.find_next("blockquote").text)

    #print(soup)
    #print(soup.prettify())
    #print(body)
    #print(body.find_all("blockquote"))
    #print(body.find_all("a"))
    print(output)

def FormatReview(company, score, review):


GamesNews()
