import pandas as pd
data1=({'A':[1,2,3],
       'B':[200,3,4]})
data2=({'A':[10,20,3],
       'B':[20,30,4]})
df1=pd.DataFrame(data1)
print(df1)
df2=pd.DataFrame(data2)
print(df2)
# operaton doing
result = df1 - df2
print(result)
result = df1 > df2
print('\n\n\n\n',result)
s1 = pd.Series([True, False, True])
s2 = pd.Series([False, False, True])

# Applying logical AND
result = s1 & s2
print(result)
# same for otehr also 
print("done")
