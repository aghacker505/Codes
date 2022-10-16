from platform import machine
import pandas as pd

# df = pd.DataFrame({"Name":["abhay", "abhi", "jonny"], 'Marks':[40, 50, 100]})
df = pd.read_csv('C:/Users/Abhay Gupta/Desktop/students.csv')
# df.head(5)
# print(df)
print(df.info())