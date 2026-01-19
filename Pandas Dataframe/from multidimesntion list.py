# import pandas as pd
import pandas as pd 
  
# List1 
lst = [['sajan', 25], ['kalo', 30],
       ['parajuli', 26], ['valu', 22]]
  
df = pd.DataFrame(lst, columns =['Name', 'Age'])
print(df)