import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv(r"C:\RecognitionV1\Dataset\all_gestures.csv")

# Split into features X and labels y
X = data.iloc[:, :-1]        # all columns except last
y = data.iloc[:, -1]         # last column is gesture label

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size= 0.2, random_state=42)\

model = RandomForestClassifier(n_estimators=150)        #150 decision trees
model.fit(X_train,y_train)

accuracy = model.score(X_test,y_test)
print(f" Model trained! Accuracy: {accuracy*100:.2f}%")

joblib.dump(model, "signLan_model.pkl")
print("Model saved as signLan_model.pkl")




