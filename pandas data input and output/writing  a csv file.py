# importing pandas as pd
import pandas as pd

# list of name, degree, score
Name = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]

# dictionary of lists
dict = {'Name': Name, 'degree': deg, 'score': scr}
    
df = pd.DataFrame(dict)
print(df)
# saving the dataframe
df.to_csv('file1.csv') # create a csv file form the datarame
df.to_csv('file2.csv',index=False) # no index willl be there 
df.to_csv("filr3.csv",header=False) 
df.to_csv("name.csv", columns = ['Name'])