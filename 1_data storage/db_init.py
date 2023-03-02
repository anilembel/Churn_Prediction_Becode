import pandas as pd
import sqlite3

# csv to dataframe
data = pd.read_csv('1_data_storage/BankChurners.csv')   
df = pd.DataFrame(data)

# dataframe to db
connexion = sqlite3.connect("1_data_storage/data.db")
df.to_sql('bankchurners', connexion, if_exists='replace', index=False)
cursor = connexion.cursor()

# db test
for row in cursor.execute('SELECT * FROM bankchurners LIMIT 3;'):
    print(row)
connexion.close()