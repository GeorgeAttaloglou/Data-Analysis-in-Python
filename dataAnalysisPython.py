import matplotlib.pyplot as plt
import csv
from datetime import date, datetime
import statistics
from collections import defaultdict

#function pou dexetai hmeromhnia apo ton xrhsth
def give_dates():
   year = int(input("Input year: "))
   month = int(input("Input month: "))
   day = int(input("Input day: "))

   given_date=date(year,month,day)
   return given_date


#mou phre 2 meres na katalabw oti den douleue epeidh den uphrxe to encoding="utf8" :)
#function gia upologismo dedomenwn
def data_stats(starting_date, ending_date):
   with open("data.csv", "r", encoding="utf8") as file:
      data = list(csv.DictReader(file, delimiter=","))
      poso = []
      
      for row in data:
         row_date = datetime.strptime(row["date_created"], "%Y-%m-%d %H:%M:%S.%f %z").date()
         if starting_date <= row_date <= ending_date:
            poso.append(float(row["poso"]))

         if not poso:
            print("No valid poso values found within the specified date range.")
            return

      sum_poso = sum(poso)
      count_poso = len(poso)
      min_poso = min(poso)
      max_poso = max(poso)
      poso_avg = sum_poso / count_poso
      sd_poso = statistics.stdev(poso)
      variance_poso = pow(sd_poso, 2)

      print("The minimum is: ", min_poso)
      print("The maximum is: ", max_poso)
      print("The average is: ", poso_avg)
      print("The standard deviation is: ", sd_poso)
      print("The variance is: ", variance_poso)

#function pou upologizei ana building id ta xrwstoumena
def show_due():
   unpaid_poso_by_building = defaultdict(float)

   with open("data.csv", "r", encoding="utf8") as file:
      data = list(csv.DictReader(file, delimiter=","))

      for row in data:
         building_id = row["buildingID"]
         poso = float(row["poso"])
         plirothike = row["plirothike"]

         if plirothike.lower() == "false":
            unpaid_poso_by_building[building_id] += poso

   for building_id, poso_sum in unpaid_poso_by_building.items():
      print(f"Building ID: {building_id}, Unpaid poso: {poso_sum}")

#function gia na deixnei ta xrwstoumena gia kathe mhna
def due_month_year():
    due_by_month_year = defaultdict(float)

    with open("data.csv", "r", encoding="utf8") as file:
        data = list(csv.DictReader(file, delimiter=","))

        for row in data:
            row_date = datetime.strptime(row["date_created"], "%Y-%m-%d %H:%M:%S.%f %z").date().month
            poso = float(row["poso"])
            plirothike = row["plirothike"]

            if plirothike.lower() == "false":
                due_by_month_year[row_date] += poso

    for row_date, poso_sum in due_by_month_year.items():
        print(f"There is: {poso_sum}, due for the {row_date} month of 2023")


#eisagwgh prwths hmeromhnias
print("Input the first date:")
starting_date = give_dates()
print ("starting date is: ", starting_date)

#eisagwgh deuterhs hmeromhnias
print("Input the final date: ")
ending_date = give_dates()
print ("ending date is: ", ending_date)

#emfanish dedomenwn
data_stats(starting_date, ending_date)

#emfanish xrwstoumenwn
show_due()

#emfanish ana mhna
due_month_year()