import os 
import csv
import pandas as pd
import matplotlib as plt

#print(f"__file__: {__file__}")
#print(f"dirname(__file__): {os.path.dirname(__file__)}")



path_forras = os.path.join(os.path.dirname(__file__), "forras")

def opcio1():
    matrix = []
    with open(os.path.join(path_forras, "directory.csv"), "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split(",")
            matrix.append(line)
            print(line)

#opcio1()

def opcio2():
    with open(os.path.join(path_forras, "directory.csv"), "r", encoding="utf-8") as f:
        data = csv.reader(f, delimiter= ",")
        for row in data:
            print(row)

#opcio2()

def opcio3():
    data = pd.read_csv(os.path.join(path_forras, "directory.csv"))
    return data

data = opcio3()
print(type(data))

data = data[["Store Name", "Street Address", "City", "Country", "Postcode", "Longitude", "Latitude"]]
magyarok = data[data["Country"] == "HU"]
chicagoiak = data[data["City"] == "Chicago"]

print(data.iloc[5, 2]) # Abu Dhabi (5.sor 2. oszlopa)
print(data.loc[5242, "City"]) # Paris

print(data.iloc[10, :])

orszagonkent = data.groupby("Country").count().reset_index("Country")
orszagonkent = orszagonkent[["Country", "Story name"]]
orszagonkent.columns = ["Country", "Story name"]
print(orszagonkent)



