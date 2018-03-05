from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

csv_file = open ("email_list.csv", "w")

url = "https://scrapebook22.appspot.com/"
response = urlopen(url).read()

soup = BeautifulSoup(response)

for link in soup.findAll("a"): # probar con .limit(5) para los 5 primeros
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        email = person_soup.find("span", attrs={"class":"email"}).string
        csv_file.write(email + "\n")

csv_file.close()
