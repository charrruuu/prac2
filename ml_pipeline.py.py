import pickle
import sys
import numpy as np
from sklearn.linear_model import LinearRegression
print("====ML CI Pipeline====")
x=np.array([[1],[2],[3]])
y=np.array([2,4,6])
mpdel=LinearRegression()
model.fit(x,y)
print("Model trained")

with open("model.pkl","wb") as f:
    pickle.dump(model,f)
print("Model saved")
prediction = model.predict([[4]])[0]
print(f"prediction:{prediction:.1f} (expacted:8:0)")
if abs(prediction - 8.0)<0.1:
    print("Validation Passed")
    sys.exit(0)
else:
    print("Validation failed")
    sys.exit(1)
    