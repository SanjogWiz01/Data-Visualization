''' Mini Projects
🔹 Project 1: Student Result Analysis

Create a DataFrame with at least 10 students having columns:
Name, Age, Gender, Department, Marks.

Perform the following:

Print students with Marks > 75.

Find the average Marks by Department (Pivot Table).

Sort the DataFrame by Marks and show the top 3 students.

Merge with another DataFrame that contains Name and City.'''
import pandas as pd
data = {'Name':['sanjog','sandhaya','poudel','ram','shyam','hari','gita','sajan','anil','juj'],
      'age':[18,19,20,46,15,25,85,96,45,8],
      'mark':[90,70,60,80,50,40,30,20,10,100],
        'department':['csit','bca','bim','csit','bca','bim','csit','bca','bim','csit'],
        'Gender':['m','f','m','m','m','m','f','m','m','f']}
df = pd.DataFrame(data)
print(df,'\n\n\n\n')
print('THE MARK OF STUDENT OVER 75 IS AS FOLLOWS\n\n\n')
print(df[df['mark']>75],'\n\n\n\n')
print('PIVORT TABLE\n\n\n\n')
a=df.pivot_table(index=['department'],values=['mark'],aggfunc='mean')
print(a,'\n\n\n\n\n','SORTED DATA ARE :\n\n\n\n')
sorted_data=df.sort_values(by='mark',ascending=False)
print(sorted_data,'\n\n\n\n')
for_3_student=df.sort_values(by='mark').head(3)
print('the top 3 student are as follows\n\n\n')
print(for_3_student)
data1 = {
    'Name':['sanjog','sandhaya','poudel','ram','shyam','hari','gita','sajan','anil','juj'],
    'Adress':['ktm','pokhara','butwal','nagpur','kanpur','allahabad','delhi','mumbai','chennai','kolkata']}
# merging name with adress
df1=pd.DataFrame(data1)
print('AFTER MERGING THE DATA \n\n\n\n')
print(pd.merge(df, df1, on='Name'))