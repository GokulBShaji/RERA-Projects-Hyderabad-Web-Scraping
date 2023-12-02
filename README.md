# RERA-Projects-Hyderabad-Web-Scraping
This project is solely done for educational purpose and is not meant for commercial use.

## Objective
To scrape all the RERA approved builder informations from MagicBricks web-site.

## Procedure
- Install scrapy using the command pip install scrapy in the terminal.
- Then in the terminal write scrapy startproject magic (as magic is the name of the project used here)
- Then create a new python file with the name magic_scraper.py inside the spiders folder and paste the code from magic_scraper.py file of this repository
- Then open the terminal and write cd magic to point the command directory to the folder with the spider
- Then there itself(in the terminal) write scrapy crawl magic -o first_run.csv
- Then create a new python file by the name cleaning.py in the main project folder i.e pythonProject_RERA/magic here.(Ensure pandas library and openpyxl library are installed in the directory of the main folder)
- Then paste the code from cleaning.py file of this repository there and run it.
- Then create a new python file with the name links_scraper.py inside the spiders folder and paste the code from links_scraper.py file of this repository
- Then open the terminal and write cd magic to point the command directory to the folder with the spider
- Then there itself(in the terminal) write scrapy crawl builder -o first_run_100.csv
- Then comment line 10 and uncomment line 11ne 11 of of links_scraper.py
- Then open the terminal and write cd magic to point the command directory to the folder with the spider
- Then there itself(in the terminal) write scrapy crawl builder -o first_run_100_200.csv
- Then comment line 11 and uncomment line 11ne 12 of of links_scraper.py
- Then open the terminal and write cd magic to point the command directory to the folder with the spider
- Then there itself(in the terminal) write scrapy crawl builder -o first_run200-300.csv
- Then comment line 12,9 and uncomment line 11ne 8,10 of of links_scraper.py
- Then open the terminal and write cd magic to point the command directory to the folder with the spider
- Then there itself(in the terminal) write scrapy crawl builder -o first_run300-rest.csv
- Then create a new python file by the name combine.py in the main project folder i.e pythonProject_RERA/magic here.
- Then paste the code from combine.py file of this repository there and run it.
- This completes the procedure and the final output is an excel file by the name Builders_Database.xlsx

 ## Results
 - There are 29 columns in the excel file (Builders_Datatbase.xlsx)
 - The Name column indicates the name of the builder project
 - The remaining 28 columns are pairs of 2 i.e column P_1 and PV_1 are pairs simlarly P_2 and PV_2 are pairs and so on till P_14 and PV_14.
 - P_1 means - Parameter 1 and PV_1 means - Parameter Value 1 and same are the cases for remaining columns

## Possible errors and suggestions
- In case of 403 error in terminal , close and relaunch the terminal
  

