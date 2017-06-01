def main():
	avg_pronouns = open('avg_pronounsTEST.txt','r')
	avg_pronouns_all_combinations = open('avg_pronouns_all_combinations.txt','w')

	avg_pronouns_all_combinations.write("Date\tFPS_TPS_SP\tFPP_TPP\tFPS_TPS\tFPP_TPP_SP\n")

	#combine the differnt pronoun types into groups
	for line in avg_pronouns:
		line = line.strip().split("\t")
		if line[2] != "avgFPS":

			date 	= line[0]
			FPS 	= float(line[2])
			FPP 	= float(line[1])
			SP 		= float(line[3])
			TPS 	= float(line[6])
			TPP 	= float(line[5])

			FPS_TPS_SP 	= round(FPS+TPS+SP,2)
			FPP_TPP 	= round(FPP+TPP,2)
			FPS_TPS 	= round(FPS+TPS,2)
			FPP_TPP_SP 	= round(FPP+TPP+SP,2)

			avg_pronouns_all_combinations.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(date,FPS_TPS_SP,FPP_TPP,FPS_TPS,FPP_TPP_SP)) #write groups to file

	

		


if __name__ == '__main__':
	main()
