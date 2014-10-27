import csv
#opens the file file_with_dup.csv to read - can be referenced as 'reader'
reader = csv.reader(open('file_with_dup.csv', 'rb'))
#opens outfile_nodup.csv to write - referenced as 'writer'
writer = csv.writer(open("outfile_nodup.csv", "wb"))
new_file= set()
#loops through 'reader'
for row in reader:
	#add an entry in new_file if it doesn't already contain it
    if row[0] not in new_file:
    	#write into 'writer'
        writer.writerow(row)
       	new_file.add( row[0] )