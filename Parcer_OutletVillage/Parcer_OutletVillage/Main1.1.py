import os
import glob
import csv
from xlsxwriter.workbook import Workbook
from bs4 import BeautifulSoup
import requests
import csv

from Model import Product


def parser(url: str):
    create_csv()
    for i in range(209, 190, -1):
        new_url = url + str(i) + "/"

        list = []
        res = requests.get(new_url)
        res.encoding = 'cp1251'
        soup = BeautifulSoup(res.text, "lxml")
        prices = soup.find_all('span', class_='woocommerce-Price-amount amount')
        old_price = prices[0].find("bdi").text
        new_price = prices[1].find("bdi").text
        description = soup.find("div", class_="ast-accordion-wrap").find("p").text
        # if price_elem:
        #     price = price_elem.get('content')
        # else:
        #     price = "По запросу"
        # list.append(Product(link=new_url,
        #                     old_price=old_price,
        #                     new_price=new_price,
        #                     description=description))
        write_csv(Product(link=new_url,
                          old_price=old_price,
                          new_price=new_price,
                          description=description))
        print(f"Sneakers {i} complete!")


def create_csv():
    with open(f"outlet-village.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "link",
            "old_price",
            "new_price",
            "description"
        ])


def write_csv(product):
    with open(f"outlet-village.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        try:
            writer.writerow([
                product.link,
                product.old_price,
                product.new_price,
                product.description
            ])
        except:
            print(product.link,
                  product.old_price,
                  product.new_price,
                  product.description)


if __name__ == '__main__':
    parser(url="https://outlet-village.online/product/nike-")
    for csvfile in glob.glob(os.path.join('.', '*.csv')):
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt', encoding='utf-8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()
