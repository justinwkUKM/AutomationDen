# __author__ = "waqasmcbookair"

import requests
from bs4 import BeautifulSoup
import smtplib
import time


# Added Two Step Verification in google for accessing email
# Created App Password by Google

URL = 'https://www.mudah.my/Kawasaki+Z800+black+phantom+fully+loaded+z8+PROMO-76731829.htm'
# URL = 'https://www.lazada.com.my/products/fossil-sport-grey-smart-watch-ftw4021-i496124600-s906322794.html?spm=a2o4k.pdp.recommendation_1.3.ff8532a834HnVs&mp=1&clickTrackInfo=31bc849e-6b3b-49e3-824c-b406cd31fc42__496124600__10100415__trigger2i__124572__0.376__0.3572__0.0__0.0__0.00843__0.358043__2__null__null__null__null__null__null__&scm=1007.16389.126158.0'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

EMAIL_FROM = 'waqasobeidy@gmail.com'
PASSWORD = 'ADD_YOUR_PASSWORD'


def check_prices():
    
    print('Checking Prices....')

    page = requests.get(URL, headers = headers)

    # print(page)

    soup = BeautifulSoup(page.content, 'html.parser')

    currency = soup.find(itemprop="priceCurrency").get("content")
    price = soup.find(itemprop="price").get("content")
    converted_price = float(price)

    # for each_div in soup.findAll('div',{'class':'complex_header'}):
    #     print(each_div.get_text().strip())

    title = soup.find('div',{'class':'complex_header'}).get_text().strip()
    print ("The price of {} is {} {}".format(title, currency, converted_price))

    if (converted_price < 25000):
        send_email()
        pass

    pass

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL_FROM, PASSWORD)

    subject = 'GingaLala'
    body = 'Jani Heres a surprise for you. You can now afford the thing you have always dreamed of buying. Go check it out now -> {}'.format(URL)
    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(EMAIL_FROM,'wko.limkokwing@gmail.com', msg)
    print('Email Sent')
    server.quit()
    
    pass

if __name__ == "__main__": 
    while True:
        check_prices()
        time.sleep(60*60)
else: 
    print ("Executed when imported")