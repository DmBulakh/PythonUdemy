import pandas
from geopy.geocoders import Nominatim

df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=["Price", "Age", "Value"], index=["First","Second"])
df2 = pandas.DataFrame([{"Name": "John", "Surname":"Johns"},{"Name":"Jack",}])
df6 = pandas.read_csv("http://pythonhow.com/supermarkets.csv")
df7 = pandas.read_json("http://pythonhow.com/supermarkets.json")
# df7=df7.set_index("Address")
# df7.loc["735 Dolores St":"332 Hill St", "Country":"ID"]
# print(df6)
# print(df7.loc["735 Dolores St":"332 Hill St", "Country":"ID"])
# print(list(df7.loc[:,"Country"]))
# print(df7.iloc[1:3,1:2])
nom = Nominatim()
df7["Address"] = df7["Address"] + ", "+df7["City"] + ", "+df7["State"]+", "+df7["Country"]
df7["Coordinates"] = df7["Address"].apply(nom.geocode)
df7["Latitude"] = df7["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df7["Longitutde"] = df7["Coordinates"].apply(lambda x: x.longitude)
print(df7)