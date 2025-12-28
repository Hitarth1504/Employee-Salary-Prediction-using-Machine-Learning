from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error
import pandas as pd

df = pd.read_csv("finaldata.csv")

x = df[['age','experience']]
y = df['salary']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=62)

model = LinearRegression()
model.fit(x_train,y_train)

pre = model.predict(x_test)
score = r2_score(y_test,pre)
print("r2 score :",score)
mae = mean_absolute_error(y_test,pre)
print("mae :",mae)

ag = float(input("Enter Your Age :"))
ex = float(input("Enter Your Experience :"))
sal = model.predict([[ag,ex]])
print(f"According to your age{ag} and Experience{ex} your sallary likely {sal}")