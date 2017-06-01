#scraper probeersel

import requests
from bs4 import BeautifulSoup

def main():
	pageTable = requests.get("http://www.gallup.com/poll/116479/barack-obama-presidential-job-approval.aspx")
	pageTable.content
	soupTable = BeautifulSoup(pageTable.content,'html.parser')

	ratings = open('ratingsTEST.txt','w') #open file the ratings must be written to
	ratings.write('DateYear\tDateMonth\tApproval\tDisapproval\n')

	id_list = [89,53,27,97,82,52,67,87] #list of id's from the tables that contain the months of Obama's ratings
	
	for i in id_list:
		table = soupTable.find('figure', id=i)
		trs = table.findChildren(['tr']) #find the <tr>s

		for tr in trs[2:-1]:

			tds = tr.find_all('td') #find <td>s
			ths = tr.find('th') #find <th>s

			#etract the date, approval and disapproval rates
			date = ths.text
			approval = tds[0].text
			disapproval = tds[1].text

			#split the date into year and month
			dateYear = date.split()[0]
			dateMonth = date.split()[1]
			
			ratings.write('{0}\t{1}\t{2}\t{3}\n'.format(dateYear,dateMonth,approval,disapproval)) #write everything to the textfile


if __name__ == '__main__':
	main()
