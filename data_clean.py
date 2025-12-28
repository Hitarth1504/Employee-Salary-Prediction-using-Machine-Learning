import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


df = pd.read_csv("dataset.csv")


print(df.isnull().sum())

#dr = df.dropna()
#print(dr)

df['age'].fillna(df['age'].mean().round(1),inplace=True)
df['experience'].fillna(df['experience'].mean().round(1),inplace=True)
df['salary'].fillna(df['salary'].mean().round(1),inplace=True)

print(df)
print(df.isnull().sum())

#encoding

df_encode = df.copy()

df_encode["name_Encoded"] = pd.get_dummies(df["name"]).astype(int).values.tolist()
df_encode["department_Encoded"] = pd.get_dummies(df["department"]).astype(int).values.tolist()
df_encode["educatiom_Encoded"] = pd.get_dummies(df["education"]).astype(int).values.tolist()

print(df_encode)


#scaling
scal = StandardScaler().fit_transform(df[['age', 'experience', 'salary']])
scal_data = pd.DataFrame(scal,columns=['age', 'experience', 'salary'])
print(scal_data)

df_final = pd.concat([scal_data, df_encode], axis=1)

print(df_final)

df_final.to_csv("finaldata.csv",index=False)