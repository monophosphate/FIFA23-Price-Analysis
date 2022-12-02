import time
from selenium import webdriver
from bs4 import BeautifulSoup


urls = ['lionel-messi/17392', 
'pierre-emerick-aubameyang/17393', 
'thomas-muller/17395', 
'phil-foden/17394', 
'niklas-sule/17396', 
'federico-valverde/17397', 
'gerard-moreno/17398', 
'patrik-schick/17410', 
'thomas-lemar/17401', 
'martin-odegaard/17400', 
'raphinha/17399', 
'bremer/17411', 
'dejan-kulusevski/17403', 
'martin-terrier/17402', 
'ibrahima-konate/17404', 
'lucas-paqueta/17412', 
'savio/17424', 
'joao-mario/17451', 
'robin-gosens/17406', 
'andre-franck-zambo-anguissa/17405', 
'aaron-wan-bissaka/17413', 
'jonathan-ikone/17407', 
'moses-simon/17408']

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("C:\chromedriver.exe", options=options)

def hr():
    print('-'*70)

def parse(url):
    driver.get(url)
    time.sleep(3)
    html = driver.page_source
    return BeautifulSoup(html, 'html.parser')

def calculate(bin, auction):
    if bin == 0 or auction == 0: return 0
    return round((auction - bin)/bin*100, 2)

def check(url):
    soup = parse(url)

    abin = soup.find('span', class_='avgbin')
    avgbin = int(abin.text.strip().replace(',', ''))

    aauc = soup.find('span', class_='avgauction')
    avgauction = int(aauc.text.strip().replace(',', ''))

    return calculate(avgbin, avgauction)

if __name__ == "__main__":
    hr()

    avgs = []
    for url in urls:
        result = check('https://www.futwiz.com/en/fifa23/player/' + url)
        avgs.append(result)
        print('URL ' + url + ' has a variance of ' + str(result) + '%')
    driver.quit()
    maxavg = max(avgs)

    hr()
    print('COMPLETE: ' + urls[avgs.index(maxavg)] + ' has the highest variance of ' + str(maxavg) + '%')
    hr()