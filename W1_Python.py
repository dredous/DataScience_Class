import numpy as np
import pandas as pd

# classes = np.array(['501', '502', '503', '504', '505', '506', '507', '508', '316'])
# timetable = np.array(np.zeros((11,len(classes)), dtype=int))
# schedules = pd.DataFrame(timetable, columns=classes)


df = pd.Series([35.2, 36.5, 36.1, 35.5, 35.0])
# print(df)
print(df.head())
print(df.describe())