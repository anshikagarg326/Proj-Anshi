from bs4 import BeautifulSoup #BS ued to scrap a website ,lxml used for parser
import requests #used to send request to a website (google) and google will send a response
#How to get html from a website

website = 'https://www.tutorialspoint.com/java/index.htm'#'https://subslikescript.com/movie/Titanic-46435'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'html.parser') 
soup.prettify()
#print(soup.encode("utf-8"))

head = soup.find('h1').get_text()
print(head)
body = soup.find('p').get_text()
print(body)

with open('tutorial.txt', 'w') as file: #created a file named tutorial in write mode and wrote body variable in it
    file.write(body)
