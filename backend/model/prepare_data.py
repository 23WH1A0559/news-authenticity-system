import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# 1. Load datasets
fake = pd.read_csv("../data/Fake.csv")
true = pd.read_csv("../data/True.csv")

# 2. Add labels
fake["label"] = 0
true["label"] = 1

# 3. Combine datasets
data = pd.concat([fake, true], axis=0)

# 4. Keep only text and label
data = data[["text", "label"]]

# 5. Shuffle dataset
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

print("Total samples:", len(data))

# 6. Split into train and test
train_data, test_data = train_test_split(
    data, test_size=0.2, random_state=42
)

# 7. Now create labeled + unlabeled split (SSL simulation)
labeled_portion = 0.3

labeled_data = train_data.sample(frac=labeled_portion, random_state=42)
unlabeled_data = train_data.drop(labeled_data.index)

# Remove labels for unlabeled data
unlabeled_data["label"] = -1

# 8. Combine again
ssl_train_data = pd.concat([labeled_data, unlabeled_data])

# 9. Save prepared datasets
ssl_train_data.to_csv("../data/ssl_train_data.csv", index=False)
test_data.to_csv("../data/test_data.csv", index=False)

print("Labeled samples:", len(labeled_data))
print("Unlabeled samples:", len(unlabeled_data))
print("Test samples:", len(test_data))