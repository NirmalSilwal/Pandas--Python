import pandas as pd
import numpy as np
import sys


df = pd.DataFrame(np.random.randn(10, 4))
##df.to_csv(sys.stdout, sep='|')


df.to_csv(sys.stdout, index=False, header=False)
