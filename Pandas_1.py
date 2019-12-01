#### Python Pandas Tutorial Video 1 and 2 By codebasics


import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("C:\Files\PIMA.csv") #read file

ab=df                                # assigning value of dataframd df
bc=df

plt.plot(df['age'])                        # ploting value of dataframe df
plt.show()                          # show the plt

# print(df.head(5))
# print(df[3:5])
#
# """
# """
#     print(bc['num_preg'][bc['age']>=50])   #conditional statement on one of the variable
#     print(ab['age'].min())                 #minimum value from age column of df dataframe
# """
# #print(df[2:5])
# plt.plot(df['age'])
# plt.show()
# print(df.columns)
# print(df.head(5))
# print(df.tail(5))
# #print(df.num_preg,df.age)
# #df.age.max()
# #print(df.describe())
# #print(df[df['age']==df['age'].min()])
# print(df.set_index('age',inplace = True))
# print(df)# change the index to column name mentioned print(df.set_index('age',inplace= true)) inplace will work like commit
# print(df.loc[21]) # call therecords by index value
# print(df.reset_index(inplace=True)) # will reset index
#
#
#
#
#
