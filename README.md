## Scraper pkt.pl
### 1. Objective of the programme
The program is used to extract contact data from the website https://www.pkt.pl/mapa-strony/firmy/a

### 2. Requirements:
- re
- request
- BeautifulSoup

### 3. Launching the script:
#### Windows

- First, launch the script main.py. Script will extract all links from the page. These links are saved to a links.txt file. 
- Then launch the script sites.py. Script will visit each link from the links.txt file and extract the target contact information: company name, address, province, phone number, tax ID and save it in the results.csv file.
### 4. TO-DO List
- adding support for all subpages (now supporting pages with letter A)
- full automation of launching
