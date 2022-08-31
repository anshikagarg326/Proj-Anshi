
# # Desktop Notifier for COVID-19

from bs4 import BeautifulSoup #BS ued to scrap a website ,lxml(I have used html.parser) used for parser
import requests #used to send request to a website (google) and google will send a response
from win10toast import ToastNotifier #used for notificataion on windows


website = 'https://www.worldometers.info/coronavirus/country/india/'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'html.parser') 

new_cases = soup.find('li', class_ ='news_li').strong.text.split()[0]
#print(new_cases)
death_cases = list(soup.find('li', class_='news_li').strong.next_siblings)[1].text.split()[0] #need to convert this into list as it prints the generator nrmlly , [1] position is for several siblings
#print(death_cases)

## Notifier
notifier = ToastNotifier()
message  = "New Cases - "+ new_cases+" Death Cases- "+death_cases
notifier.show_toast(title="COVID-19 Update", msg=message, duration=5, icon_path="virus.ico")