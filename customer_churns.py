import pandas as pd

df = pd.read_csv("dataset/customer_churn_dataset-testing-master.csv")
print(df.shape)
df.head()