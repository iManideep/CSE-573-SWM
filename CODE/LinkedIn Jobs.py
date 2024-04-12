import csv
import requests
from bs4 import BeautifulSoup
 
file = open('linkedin-jobs.csv', 'a', newline='')
writer = csv.writer(file)
writer.writerow(['Title', 'Company', 'Location', 'Apply'])
 
def linkedin_scraper(webpage, page_number):
	next_page = webpage +"&start=" +str(page_number)
	print(str(next_page))
	response = requests.get(str(next_page))
	soup = BeautifulSoup(response.content,'html.parser')
 
	jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
	for job in jobs:
		job_title = job.find('h3', class_='base-search-card__title').text.strip()
		job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
		job_location = job.find('span', class_='job-search-card__location').text.strip()
		job_link = job.find('a', class_='base-card__full-link')['href']
		 
		writer.writerow([
		job_title,
		job_company,
		job_location,
		job_link
		])
	 
	print('Data updated')
	 
	if page_number < 1000:
		page_number = page_number + 25
		linkedin_scraper(webpage, page_number)
	else:
		file.close()
		print('File closed')
# linkedin_scraper('https://www.linkedin.com/jobs/search/?currentJobId=3655157516&keywords=Software%20Engineer&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true', 0)
linkedin_scraper('https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=United%20States&locationId=&geoId=103644278&f_TPR=r86400&position=1&pageNum=0', 0)
