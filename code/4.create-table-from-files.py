import pandas as pd
from sqlalchemy import create_engine
import os

#get name file
file_path= r'/home/sakabuana31/DigitalSkola/3.Project3_batch-prosessing/source/users_w_postal_code.csv'
file_name= os.path.basename(file_path).split('.')[0]

#create data framework
df=pd.read_csv('/home/sakabuana31/DigitalSkola/3.Project3_batch-prosessing/source/users_w_postal_code.csv', sep=',')

#manipulasi data
df['email']=df['email'].apply(lambda x: x.split('@')[0])

#create engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
df.to_sql(file_name, engine)