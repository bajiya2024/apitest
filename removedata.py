#remove the special elements from the columns 
#special elements are IN/ which are located in the pin code column starting 


import csv
import string 

#open csv file 
input_file = open('IN.csv', 'r')

#save in csv file (after remove special elements)
output_file = open('csv_data.csv', 'w')
data = csv.reader(input_file)
writer = csv.writer(output_file)
specials = 'IN/'


for line in data:
    line = [value.replace(specials, '') for value in line]
    writer.writerow(line)
input_file.close()
output_file.close() 