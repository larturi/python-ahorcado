from lxml import html
import requests

def get_word():
    page = requests.get('https://www.palabrasaleatorias.com/?fs=1&fs2=0&Submit=Nueva+palabra')
    tree = html.fromstring(page.content)
    word = tree.xpath('//div/text()')[0].strip()
    
    return word
