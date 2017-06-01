from operator import itemgetter

def main():
	ratings = open('ratings.txt','r')
	avg_ratings = open('avg_ratingsTEST.txt','w')

	avg_approval_rating_dict = {}
	avg_disapproval_rating_dict = {}

	for rating in ratings:
		rating = rating.split('\t')

		year = rating[0]
		month = rating[1]
		#names of the month converted to numbers, done for the sorting later
		if month == "Jan":
			month = "01"
		if month == "Feb":
			month = "02"
		if month == "Mar":
			month = "03"
		if month == "Apr":
			month = "04"
		if month == "May":
			month = "05"
		elif month == "Jun":
			month = "06"
		elif month == "Jul":
			month = "07"
		if month == "Aug":
			month = "08"
		if month == "Sep":
			month = "09"
		if month == "Oct":
			month = "10"
		if month == "Nov":
			month = "11"
		elif month == "Dec":
			month = "12"
		approval = rating[2]
		disapproval = rating[3]

		if year != "DateYear": #skip first line

			#create dictionairies with values per Month per Year
			if year not in avg_approval_rating_dict:
				avg_approval_rating_dict[year] = {month:[approval]}
			else:
				if month not in avg_approval_rating_dict[year]:
					avg_approval_rating_dict[year][month] = [approval]
				else:
					avg_approval_rating_dict[year][month].append(approval)
			
			#create dictionairies with values per Month per Year
			if year not in avg_disapproval_rating_dict:
				avg_disapproval_rating_dict[year] = {month:[disapproval]}
			else:
				if month not in avg_disapproval_rating_dict[year]:
					avg_disapproval_rating_dict[year][month] = [disapproval]
				else:
					avg_disapproval_rating_dict[year][month].append(disapproval)


	list_with_everything = []

	#to sort according to date, everything is put in a list
	for year in avg_approval_rating_dict: #year
		for month in avg_approval_rating_dict[year]: #month
			total = 0
			for value in avg_approval_rating_dict[year][month]:
				total += int(value)
			avg = total/len(avg_approval_rating_dict[year][month])
			list_with_everything.append(["approval",year,month,avg])

	for year in avg_disapproval_rating_dict: #year
		for month in avg_disapproval_rating_dict[year]: #month
			total = 0
			for value in avg_disapproval_rating_dict[year][month]:
				total += int(value)
			avg = total/len(avg_disapproval_rating_dict[year][month])
			list_with_everything.append(["disapproval",year,month,avg])


	sorted_list_with_everything = sorted(list_with_everything, key=itemgetter(0,1,2)) #sort items first on year, then on month

	for i in sorted_list_with_everything:
		avg_ratings.write("{0}-{1}\t{2}\t{3}\n".format(i[1],i[2],i[3],i[0])) #writed sorted items to file, year-month,avg,(dis)approval 

if __name__ == '__main__':
	main()