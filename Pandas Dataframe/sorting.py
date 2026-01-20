import pandas as pd

data = {'name': ['sanjog', 'poudel', 'ram', 'shyam'],
        'age': [10, 50, 80, 40],
        'score': [90, 70, 60, 80]}

df = pd.DataFrame(data)

print(df,'\n\n\n\n\n')
# single sorting

sorted_data = df.sort_values(by='age', ascending=False)

print('\n\n\n\n\n',sorted_data,'\n\n\n\n\n')
# multiple sorting
sorted_data2=df.sort_values(by=['age','score'],ascending=[True,True])
print(sorted_data2,'\n\n\n\n\n')
# sort by index
sorted_data3=df.sort_index()
print(sorted_data3,'\n\n\n\n\n')
#quick sort
sorted_data4=df.sort_values(by='age',kind='quicksort')
print(sorted_data4,'\n\n\n\n\n')
#mergesort
sorted_data5=df.sort_values(by='age',kind='mergesort')
print(sorted_data5,'\n\n\n\n\n')
#heapsort
sorted_data6=df.sort_values(by='age',kind='heapsort')
print(sorted_data6,'\n\n\n\n\n')
#stable
sorted_data7=df.sort_values(by='age',kind='stable')
print(sorted_data7,'\n\n\n\n\n')


