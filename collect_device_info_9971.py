import pandas as pd
import requests
from bs4 import BeautifulSoup

with open("cisco_9971.txt") as file:
	for ip_add in file:
		if "http" in ip_add:
		#browser = webdriver.Chrome()
			page = requests.get(ip_add.strip())
#with open('view-source10-90-52-85.html') as page_content:
			soup = BeautifulSoup(page.content, 'html.parser')

#print(soup)
			device_information = soup.find('div', align="center")
		#print(device_information)

			target = device_information.find_all(tr='')
			#print(target[5].get_text())
			#print(target[18].get_text())
			#print(target[41].get_text())

		#print(ip_add)
		MAC_Address = [(target[12].get_text())]
		Ext = [(target[30].get_text())]
		Serial_Number = [(target[66].get_text())]
		Model_Number = [(target[72].get_text())]
		#print(MAC_Address)
		#print(Ext)
		#print(Serial_Number)

			#mac_address = [info.tr.find('MAC Address').get_text() for info in target]
			#print(mac_address)


#print(target[0].find(b='').get_text())

		all_info = pd.DataFrame(
			{
				'MAC_Address': MAC_Address,
	 			'EXT.': Ext,
	 			'Serial_Number': Serial_Number,
	 			'Model_Number': Model_Number,
			})
		print(all_info)

		#all_info.to_csv(f'Device_Information_Model_8865.csv', index=True)
