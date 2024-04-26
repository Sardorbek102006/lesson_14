from bs4 import BeautifulSoup
from malumot import infor

url = "https://asaxiy.uz/product/kompyutery-i-orgtehnika/noutbuki/noutbuki-2"
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
menu = soup.find("div", class_="row")
products = menu.find_all("div", class_="col-6")

for product in products:
    image = product.find("img", class_="img-fluid")["data-src"]
    tovar_name = product.find('span', class_='product__item__info-title').get_text().strip()
    str_product_name = str(tovar_name).strip()
    product_price = product.find('span', class_='product__item-price').get_text()
    credit_price = product.find('div', class_='installment__price').get_text()
    data_month = str(credit_price)
    #alls = tovar_name, image, product_price, credit_price
    infor(image, tovar_name, product_price, data_month)

    print('hamasi zor')