from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.google.co.in/search?dcr=0&ei=LN-_WuPAIsSKvQT6kY_wAg&q=cricket+score&oq=crick&gs_l=psy-ab.3.2.0j0i67k1l2j0i10i67k1j0j0i131k1j0j0i10i67k1j0j0i10k1.552188.556069.0.559936.6.6.0.0.0.0.121.535.0j5.6.0....0...1c.1.64.psy-ab..0.5.533.0..0i131i67k1.64.yBjP5Xj2of0#sie=lg;/g/11c6s1y70g;5;/m/021q23;mt;fp;1').text

soup = BeautifulSoup(source,'lxml')

links = soup.find('h3')

links = links.a.text

print(links)
