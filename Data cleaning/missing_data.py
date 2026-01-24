# Python program to detect mixed data types in Pandas data frame

# Import the library Pandas
import pandas as pd
  
# Create the pandas DataFrame
data_frame = pd.DataFrame( [['tom', 10], ['nick', '15'], ['juli', 14.8]], columns=['Name', 'Age'])

# Traverse data frame to detect mixed data types
for column in data_frame.columns:
    print(column,':',pd.api.types.infer_dtype(data_frame[column]))