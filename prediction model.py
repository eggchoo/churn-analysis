import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split    
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder 
import joblib

file_path = r"C:\Users\08042\Desktop\churn project\prediction model.xlsx"
sheet_name='vw_ChurnData'
data = pd.read_excel(file_path, sheet_name=sheet_name)
print(data.head())

data=data.drop(columns=['Customer_ID','Churn_Category','Churn_Reason']) #removing the last 2 columns as they are not needed for prediction

columns_to_encode = ['Gender', 'Married', 'State','Value_Deal','Phone_Service','Multiple_Lines', #assigning code based on aplhabetical order e.g. F=0, M=1
                     'Internet_Service','Internet_Type','Online_Security','Online_Backup',
                     'Device_Protection_Plan','Premium_Support','Streaming_TV','Streaming_Movies','Streaming_Music',
                     'Unlimited_Data','Contract','Paperless_Billing','Payment_Method']

# encoding categorical variables into numeric variables except 'Customer_Status' column
label_encoders = {}
for column in columns_to_encode:
    label_encoders[column] = LabelEncoder() 
    data[column] = label_encoders[column].fit_transform(data[column])

# mannually encoding 'Customer_Status' column
data['Customer_Status'] = data['Customer_Status'].map({'Stayed': 0, 'Churned': 1})

# Splitting the data into features and target variable (independent and dependent variables)
X = data.drop('Customer_Status', axis=1)  # Features
y = data['Customer_Status']               # Target variable

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
# 20% test size and 80% train size is a common split, random_state=42 ensures reproducibility

# Initializing and training the Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
# n_estimators=100 means the model will use 100 decision trees in the forest

# Fitting the model on the training data
rf_model.fit(X_train, y_train)

# Making predictions on the test data
y_pred = rf_model.predict(X_test)

# Evaluating the model's performance
print("Confusion Matrix:")  
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# feature importance
feature_importances = rf_model.feature_importances_
indices = np.argsort(feature_importances)[::-1] # Sort features by importance in descending order [::-1] means reverse order

# plotting feature importance
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
sns.barplot(x=feature_importances[indices], y=X.columns[indices])
plt.title("Feature Importances")
plt.xlabel("Relative Importance")
plt.ylabel("Feature Names")
plt.show()


# preict new data
new_file_path = r"C:\Users\08042\Desktop\churn project\prediction model.xlsx"
new_sheet_name='vw_JoinData'
new_data = pd.read_excel(new_file_path, sheet_name=new_sheet_name)
print(new_data.head())

original_data=new_data.copy() #keeping a copy of original data for reference
cutomers_ids = new_data['Customer_ID'] #storing customer ids for reference
new_data=new_data.drop(['Customer_ID','Customer_Status','Churn_Category','Churn_Reason'], axis=1) #removing the last 3 columns as they are not needed for prediction

# encoding categorical variables into numeric variables except 'Customer_Status' column
for column in new_data.select_dtypes(include=['object']).columns: 
    new_data[column] = label_encoders[column].fit_transform(new_data[column])


# Making predictions on the test data
new_prediction = rf_model.predict(new_data)

# Adding predictions to the new_data DataFrame
original_data['Customer_Status_Predicted'] = new_prediction

# filtering churned customers
original_data= original_data[original_data['Customer_Status_Predicted'] == 1]

# saving the predictions to a new Excel file
original_data.to_csv(r"C:\Users\08042\Desktop\churn project\churn_predictions.csv", index=False)



