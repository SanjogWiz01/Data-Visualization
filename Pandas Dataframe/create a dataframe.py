import pandas as pd
a=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
# Output:
#               Bob           Sue
# Product A  I liked it.  Pretty good.
# Product B   It was awful.       Bland.
print(a)