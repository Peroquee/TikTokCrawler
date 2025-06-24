import csv
from robot.api.deco import keyword

class manageCSV:
    @keyword
    def schreibe_CSV(self,output):
        with open(".idea\\output_csv\\links.csv", mode="a+",newline='',encoding="utf-8") as datei:
            writer = csv.writer(datei)

            writer.writerow([output])