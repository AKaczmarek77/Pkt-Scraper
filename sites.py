from bs4 import BeautifulSoup
from requests import get
import re


results = open('results.csv', 'a')
links = open("links.txt", 'r').readlines()
for link in links:
    url = link
    page = get(url)
    bs = BeautifulSoup(page.content, 'html.parser')

    for item in bs.find_all('div', class_="box-detail container cf"):
        company_name = item.find('h1', class_="company-name").text
        try:
            company_street = item.find('div', class_="box-company-street").text
        except:
            company_street = 'null'
        try:
            company_email = item.find('div', class_="call-cell call--email")
            company_email = re.search('title=\"(.*)\"><', str(company_email))
            company_email = str(company_email[0])
            company_email = company_email.replace('title="Email"> <span data-tooltip="tooltip" title="', '')
            company_email = company_email.replace('"><i class="icon icon--email"><', '')
        except:
            company_email = 'null'
        try:
            company_nip = item.find('div', class_="full-company-data-box__nip").text
        except:
            company_nip = 'null'
        try:
            company_number = item.find('a', class_="attr_shownumber").get("data-phone")
        except:
            company_number = 'null'

        data_set = company_name + ";" + company_street + ";" + company_number + ";" + company_email + ";" + company_nip
        print(data_set)

        results.write(data_set + "\n")
results.close()


