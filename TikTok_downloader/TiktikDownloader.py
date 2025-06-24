import pyktok as pyk
import csv

#pyk.specify_browser('edge')

with open(".idea\\output_csv\\links.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        pyk.save_tiktok(row[0], True)

