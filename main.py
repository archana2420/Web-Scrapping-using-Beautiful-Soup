import requests
from bs4 import BeautifulSoup
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Java+Developer&txtLocation="

# Get the HTML
r = requests.get(url)
htmlContent = r.content

# Creating Soup(Parse the HTML)
soup = BeautifulSoup(htmlContent,'html.parser')

companies=soup.findAll('h3',class_="joblist-comp-name")

for i in companies:
    print("-----------------------------------------------")
    print("Company Name:",i.get_text())
    info=soup.find('li',class_="clearfix job-bx wht-shd-bx")
    skills = info.findAll('span', class_="srp-skills")
   
    for i in skills:
        print("Skills:",i.get_text())
    
