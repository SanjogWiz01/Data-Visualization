import pandas as pd

df = pd.DataFrame([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
                  index=['row 1', 'row 2', 'row 3'],
                  columns=['col 1', 'col 2', 'col 3'])

df.to_json('file1.json')

df = pd.read_json('file1.json') # ,orient='split', compression='infer'  # orient='records' foe reemoving rowsc
print(df)
# this willl be write the json file in the current working directory