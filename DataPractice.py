import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#df = pd.read_excel(r'C:\Users\h2pro\Programming\coalpublic2013.xls')
#print(df.head)

#series_obj = Series(np.arange(8), index=['row 1', 'row 2','row 3','row 4', 'row 5', 'row 6', 'row 7','row 8'])
np.random.seed(25)

DF_obj = DataFrame(np.random.rand(36).reshape((6,6)),
                  index=['row 1', 'row 2','row 3','row 4', 'row 5', 'row 6'],
                  columns=['column 1','column 2','column 3','column 4','column 5','column 6',])

print(DF_obj.loc[['row 2','row 5'], ['column 5', 'column 2']])
print(DF_obj < .2)



