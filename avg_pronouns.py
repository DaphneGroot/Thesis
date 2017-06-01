from operator import itemgetter

def main():
	pronouns = open('LIWC2015 Results (Na_inauguratie (379 files)) - alleen pronouns.txt','r')
	avg_pronouns = open('avg_pronounsTEST.txt','w')

	avg_pronouns.write("DateYear-DateMonth\tavgFPP\tavgFPS\tavgSP\tavgTP\tavgTPP\tavgTPS\n")

	avg_pronoun_dict = {}

	for pronoun in pronouns:
		pronoun = pronoun.strip().split('\t')

		filename = pronoun[0]
		TP = pronoun[3] #TotalPronouns
		FPS = pronoun[4] #FirstPersonSingular
		FPP = pronoun[5] #FirstPersonPlural
		SP = pronoun[6] #SecondPerson
		TPS = pronoun[7] #ThirdPersonSingular
		TPP = pronoun[8] #ThirdPersonPlural

		if filename != "Filename": #skip first line
			#get date from filename
			dateYear = filename.split("-")[0]
			dateMonth = filename.split("-")[1]

			#create dictionairies with values per Month per Year
			if dateYear not in avg_pronoun_dict:
				avg_pronoun_dict[dateYear] = {dateMonth:{"TP":[TP],"FPS":[FPS],"FPP":[FPP],"SP":[SP],"TPS":[TPS],"TPP":[TPP],}}
			else:
				if dateMonth not in avg_pronoun_dict[dateYear]:
					avg_pronoun_dict[dateYear][dateMonth] = {"TP":[TP],"FPS":[FPS],"FPP":[FPP],"SP":[SP],"TPS":[TPS],"TPP":[TPP],}
				else:
					avg_pronoun_dict[dateYear][dateMonth]["TP"].append(TP)
					avg_pronoun_dict[dateYear][dateMonth]["FPS"].append(FPS)
					avg_pronoun_dict[dateYear][dateMonth]["FPP"].append(FPP)
					avg_pronoun_dict[dateYear][dateMonth]["SP"].append(SP)
					avg_pronoun_dict[dateYear][dateMonth]["TPS"].append(TPS)
					avg_pronoun_dict[dateYear][dateMonth]["TPP"].append(TPP)

	#to sort according to date, everything is put in a list
	list_with_everything = []
	for year in avg_pronoun_dict: #year
		for month in avg_pronoun_dict[year]: #month
			avg_list = []
			for pronoun_type in avg_pronoun_dict[year][month]:
				total = 0
				for value in avg_pronoun_dict[year][month][pronoun_type]:
					value = value.replace(",",".") #replace , with. so it's convertable to float
					total += float(value)
				avg = round(total/len(avg_pronoun_dict[year][month][pronoun_type]),2)
				avg_list.append([pronoun_type,avg])

			avg_list.sort()
			list_with_everything.append([year,month,avg_list[0][1],avg_list[1][1],avg_list[2][1],avg_list[3][1],avg_list[4][1],avg_list[5][1]])
			
	sorted_list_with_everything = sorted(list_with_everything, key=itemgetter(0,1)) #sort items first on year, then on month

	for i in sorted_list_with_everything:
		avg_pronouns.write("{0}-{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\n".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])) #writed sorted items to file

if __name__ == '__main__':
	main()