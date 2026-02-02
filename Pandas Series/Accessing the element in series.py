import pandas as pd
import numpy as np
data=np.array([12,4,5,6,7])
print(' the series dat are',pd.Series(data))
# acessing the data of e given
print(pd.Series(data)[:2])
print(pd.Series(data).head(2))
print(pd.Series(data[2]))
# multiple acessing
# import pandas and numpy
import pandas as pd
import numpy as np

# creating simple array
data = np.array(['s', 'a', 'n', 'j', 'o', 'g',
                 'p', 'o', 'u', 'd', 'e', 'l'])
ser = pd.Series(data, index=[10, 11, 12, 13, 14,
                             15, 16, 17, 18, 19, 20, 21])

# accessing a multiple element using
# index element
print(ser[[10, 11, 12, 13]])
er = pd.Series(np.arange(3, 9), index=['a', 'b', 'c', 'd', 'e', 'f'])
print(er)
