#Covid19.py
file = open("covid19_data.csv","r")
file_new = open("covid19_infomation_clean_data.csv", "w")

header = file.readline()
file_new.write("Date, Local, Region, New_case, Total_case, Population\n")
row = file.readline()
while row != "":
	
	row_list = row.split(",")
	date = row_list[3]
	local = row_list[1]
	region = row_list[2]
	new_case = row_list[5]
	total_case = row_list[4]
	population = row_list[48]
	row_new = date + "," + local + "," + region + "," + new_case + "," + total_case + "," + population + "\n"
	file_new.write(row_new)
	row = file.readline()
