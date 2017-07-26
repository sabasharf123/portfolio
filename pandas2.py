import pandas
data = pandas.read_csv("data/weather_year.csv")
#print(data)
#print(data.columns)
#print(len(data))
#print(data.EDT)
print(data.EDT.head(10))
print (data.EDT.tail(10))
