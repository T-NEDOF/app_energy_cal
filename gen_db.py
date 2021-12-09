import csv
import pickle
import os

# case1
# with open(r"C:\Users\Tien Vu\Desktop\GCP\app_energy_calc\energy-calc\db\db.csv") as f:
#   data = csv.reader(f)

# case 2
# with open("C:/Users/Tien Vu/Desktop/GCP/app_energy_calc/energy-calc/db/db.csv") as f1:
#   __DB__ = csv.reader(f1)

# with open("C:/Users/Tien Vu/Desktop/GCP/app_energy_calc/energy-calc/db/db.pickle") as f2:
#   __pickle_file__ = csv.reader(f2)

__DB__ = os.path.join(os.getcwd(), "db/", "db.csv")
__pickle_file__ = os.path.join(os.getcwd(), "db/", "db.pickle")

reader = csv.reader(open(__DB__, "r"))
keys = next(reader)


db = []
for row in reader:
    r = dict(zip(keys, row))
    db.append(r)

pickle.dump(db, open(__pickle_file__, "wb"))
print(db)

