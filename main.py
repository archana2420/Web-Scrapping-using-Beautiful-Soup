import requests
from bs4 import BeautifulSoup
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Java+Developer&txtLocation="

# Get the HTML
r = requests.get(url)
htmlContent = r.content

# Creating Soup(Parse the HTML)
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup)
# HTML Tree traversal
# title_tag = soup.title
# print(meta_tag)

companies=soup.findAll('h3',class_="joblist-comp-name")
# print("Company Names")
for i in companies:
    print("-----------------------------------------------")
    print("Company Name:",i.get_text())
    info=soup.find('li',class_="clearfix job-bx wht-shd-bx")
    skills = info.findAll('span', class_="srp-skills")
    # location=info.findAll('ul',class_="top-jd-dtl clearfix")
    for i in skills:
        print("Skills:",i.get_text())
    # city=location.findAll('span')
    # print(locations)
    # for i in location['span']:
    #     print(i['title'])

    # print(info.find('span',class_="srp-skills").get_text)
# skills=soup.findAll('span',class_="srp-skills")
# print("Skills :")
# for i in skills:
#     print(i.get_text())
# info=soup.findAll('ul',class_="new-joblist")
# # locations=info.findAll('li')
# city=info.findAll('span')
# # print(locations)
# for i in city:
#     print(i['title'])
