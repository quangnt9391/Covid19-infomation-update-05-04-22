import datetime
file_new = open("covid19_infomation_clean_data.csv","r")
file_total_case = open("covid19_total_case.csv", "w")
file_total_case.write("Local, Region, Total_Case, Population\n")
row_new = file_new.readline() 
while row_new != "":
	row_new_list = row_new.split(",")
	date = row_new_list[0]
	local = row_new_list[1]
	region = row_new_list[2]
	total_case = row_new_list[4]
	population = row_new_list[5]
	while local != "":
		if date == "2022-04-04":
			row_total = local + "," + region + "," + total_case + "," + population
			file_total_case.write(row_total)
		break
	row_new = file_new.readline()
