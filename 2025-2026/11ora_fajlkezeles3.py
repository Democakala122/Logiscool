import pandas as pd
import numpy as np
import os 

FORRAS_PATH = os.path.dirname(__file__)
FORRAS_PATH = os.path.join(FORRAS_PATH, "forras")

pd.set_option('display.max_columns', None)

data = pd.read_csv(os.path.join(FORRAS_PATH, "library.csv"))
print(data.columns) # Oszlopok nevei
data = data.drop(['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 
                  'Issuance type', 'Contributors'], axis=1)

data = data.drop(columns=['Shelfmarks'])

print(data.head)

#Indexeljük újra a táblázatot (DataFrame), az új sorindex legyen az Identifier értéke
print(data["Identifier"].is_unique) # Leelenőrizzük, hogy az Identifier unique (egyedi) - e
#True -> Minden identifier egyedi -> alkalmas sorok indexelésére
data = data.set_index("Identifier")

print(data.head) 
print(data.loc[1143]) # 1143-as ID-ju könyvet
print(data.iloc[1143]) # Ez már egy másik könyv (1143 + 1)
print(data.loc[1143, 'Author']) # A., T.

# Adatok elég zavarosak, le kellene őket tisztítani
# Tisztítsuk le a Date of Publication és Place of Publication oszlopokat
#print(data['Date of Publication'].head(20))
year = data["Date of Publication"].str.extract(r"(\d{4})", expand=False)
print(year)
data["Date of Publication"] = year.astype("Int16")
print(data.head(20))

# A hiányzó értékeket is kezeljük le valahogyan
print("null értékek száma (Date oszlop):", data['Date of Publication'].isnull().sum())
atlag = round(data['Date of Publication'].mean())
data['Date of Publication'] = data['Date of Publication'].fillna(atlag)

places = (data['Place of Publication'].str.replace(r"[\[\]]", "", regex=True)
            .str.split(r"[;,:]", n = 1))