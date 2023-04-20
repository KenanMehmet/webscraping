from requests_html import HTMLSession

s = HTMLSession()

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'
query = 'bexley'
url = f'https://www.google.com/search?q=weather+{query}'

r = s.get(url, headers={'User-Agent': user_agent})

temp = r.html.find('span#wob_tm', first=True).text

units = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text

description = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

print(temp, units, description)