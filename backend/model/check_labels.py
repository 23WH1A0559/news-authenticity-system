import pandas as pd

data = pd.read_csv("../data/ssl_train_data.csv")
print(data["label"].value_counts())