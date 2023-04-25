import numpy as np 
import pandas as pd 

rng = np.random.default_rng(123) 

d = rng.random((3, 3))
print(d) 

print(pd.DataFrame(data = d))
