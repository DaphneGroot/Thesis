#scraper probeersel

import requests
from bs4 import BeautifulSoup

def getSpeech(link,dateYear,dateMonth,dateDay):
	pageSpeech = requests.get("http://www.americanrhetoric.com/{0}".format(link)) #go to the page with the speech
	pageSpeech.content

	soupSpeech = BeautifulSoup(pageSpeech.content,'html.parser')

	speechText = soupSpeech.find_all('font', face='Verdana') #find every textpart with the right font (font of the table)

	#convert the months as strings to the months as numbers
	if dateMonth == "January":
		dateMonth = "01"
	if dateMonth == "February":
		dateMonth = "02"
	if dateMonth == "March":
		dateMonth = "03"
	if dateMonth == "April":
		dateMonth = "04"
	if dateMonth == "May":
		dateMonth = "05"
	elif dateMonth == "June":
		dateMonth = "06"
	elif dateMonth == "July":
		dateMonth = "07"
	if dateMonth == "August":
		dateMonth = "08"
	if dateMonth == "September":
		dateMonth = "09"
	if dateMonth == "October":
		dateMonth = "10"
	if dateMonth == "November":
		dateMonth = "11"
	elif dateMonth == "December":
		dateMonth = "12"
	
	#create new file
	speech = open('speeches/Alle/test/{0}-{1}-{2}.txt'.format(dateYear,dateMonth,dateDay),'w')

	#write content of speech to textfile
	for item in speechText:
		text = item.get_text()
		
		speech.write(text)
		speech.write('\n')

	return True



def main():
	pageTable = requests.get("http://www.americanrhetoric.com/barackobamaspeeches.htm")
	pageTable.content
	soupTable = BeautifulSoup(pageTable.content,'html.parser')

	tabel = soupTable.find_all('table', id='AutoNumber1') #find the right table on the 'main' webpage 

	numberOfSpeeches = 0 #calculate number of speeches as well
	data = []

	for tr in soupTable.find_all('tr')[2:-2]: #for every <tr>, starting by the second until the one to last

		tds = tr.find_all('td') #find the <td>s
		link = tds[1].find('a').get('href') #get the link
		date = tds[0].text #get the date

		#split the date into year, month, day
		dateYear = date.split()[2]
		dateMonth = date.split()[1]
		dateDay = date.split()[0]

		numberOfSpeeches += 1
		uitkomst = getSpeech(link,dateYear,dateMonth,dateDay,title) #give evrything to the funtion
		print(numberOfSpeeches)


if __name__ == '__main__':
	main()
