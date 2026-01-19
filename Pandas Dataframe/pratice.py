import numpy as np
import pandas as pd
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])          
print(matrix)
q={'Name':[matrix],
   'age':[1,2,3,4,5,6,7]}
p=pd.DataFrame(q)
print(p)