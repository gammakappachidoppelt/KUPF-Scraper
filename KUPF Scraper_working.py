import requests
from bs4 import BeautifulSoup
import datetime

def enough_time_to_apply(date_str):
        if (date_str == "Keine Angabe") or (date_str==""):
          return False
       
        date = datetime.datetime.strptime(date_str, '%d.%m.%Y')
        now = datetime.datetime.now()
        seven_days_between = date - now >= datetime.timedelta(days=7)
        
        return seven_days_between

file = r"C:\Users\hilfe\Desktop\Sonstiges\Python Projects\Webscraping\Jobsuche\KUPF Scraper\Jobs_Kupf.txt"

with open(file, 'w', encoding="utf-8") as f:
        num = 1
        
        while(True):
                response = requests.get(f'https://www.kupf.at/kulturjobs/page/{num}')
                soup = BeautifulSoup(response.text, 'html.parser')
                job_listings = soup.find_all(class_='kulturjob')

                if job_listings == []:
                        f.write("------------------------------\n\n")
                        break

                for job in job_listings:
                        deadline = info[2].text.strip().split('\n')[1]

                        if enough_time_to_apply(deadline):
                                title = job.find("h2", class_="entry-title").text 
                                company_field = job.find("h3") 
                                company_field = str(company_field).partition("<h3>")
                                company = company_field[2].partition("</h3>")[0] 
                                info = job.find_all(class_='kulturjobs-icon-row-excerpt')
                                salary = info[0].text.strip().split('\n')[1]
                                hours = info[1].text.strip().split('\n')[1]
                                
                                
                                f.write(f'Titel: {title}\nFirma: {company}\nBruttolohn: {salary}\nStundenausmaß: {hours}\nBewerbungsfrist: {deadline}\n\n')

                num += 1

