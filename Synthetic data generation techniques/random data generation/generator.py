# sample program:
import pandas as pd
import numpy as np

# generate 1000 samples from a normal distributions
heights = np.random.normal(loc=170, scale=10, size=1000)
weights = np.random.normal(loc=70, scale=15, size=1000)

# Create a new correlation between height and weight. 
weights += (heights - 170) * 0.5
df = pd.DataFrame({'Height': heights, 'Weight': weights})

# add categorial data :
genders = np.random.choice(['Male', 'Female'], size=1000)
df['Gender'] = genders
df.head()
df.describe()
