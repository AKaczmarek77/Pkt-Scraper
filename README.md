## Scraper pkt.pl

### 1. Objective of the programme

The program is used to extract contact data from the website pkt.pl

### 2. Requirements:

- re
- request
- BeautifulSoup

### 3. Launching the script:

Windows

Just run the script, the program runs and writes contact data to output.csv file
After starting the program will print out in the console the currently processed pages and possible messages about lack of access to the site (this happens when there is no content or server error is returned).

### 4. Debugging

If the program encounters an unsupported exception to access a particular page, the action will be terminated. An error message will appear in the console. Then you should:
Add the exception to the code
For a quick resume, you need to find the last entered domain in the output.csv file. Then find it in the input and delete all records until it occurs.
 
 ### 5. TODO LIST
- adding support for all subpages (now supporting pages with letter A)
- filtering output from duplicates
- input reading improvement (http://)
