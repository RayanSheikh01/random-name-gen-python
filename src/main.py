import random
import pandas as pd

names = pd.read_csv('babynames-clean.csv')
sex = input("What is the sex of the name you would like generated: (boy or girl) ")
index = random.randint(1, len(names))
while names.loc[index, 'sex'] != sex:
    index = random.randint(1, len(names))

name = names.loc[index, 'name']
print(name)
