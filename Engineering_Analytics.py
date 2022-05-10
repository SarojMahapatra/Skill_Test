import os
import json 
import csv
import sys

try:
    watch_directory = sys.argv[1]
except:
    watch_directory = 'Local_Path_of_the_file'

output_file = os.path.join(watch_directory,'Combined.csv')


files = [ x for x in os.listdir(watch_directory) if x.endswith('.csv') ]

#print(files)

if 'Combined.csv' in files: files.remove('Combined.csv')

if not files:
    print("no files to process")
    sys.exit(0)

def generate_combined_out(file_list):

    out = []

    for file in file_list:
        file_path = os.path.join(watch_directory,file)
        with open(file_path,'r') as f:
            opened_file = csv.reader(f)
            for row in list(opened_file)[1:]:
                out.append(
                    {
                        "Source IP":row[0],
                        "Environment": file
                    }
                )

    return list({x['Source IP']:x for x in out}.values())



def write_csv_file(dict_data):
    csv_column = ["Source IP","Environment"]

    try:
        with open(output_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_column)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")

        

data = generate_combined_out(files)
print(data)
write_csv_file(data)
