import numpy as np
import pandas as pd

notes = {"Math": 80, "Software": 85, "Electronic": 75, "Physic": 60}
seri1 = pd.Series(notes)
print(seri1 * 1.05)

