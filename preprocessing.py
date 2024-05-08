import pandas as pd

# Load data into a pandas dataframe
data = pd.read_csv('diabetes_data_upload')

# Convert categorical columns to binary
data['Gender'] = data['Gender'].apply(lambda x: 1 if x == 'Male' else 0)
data['Polyuria'] = data['Polyuria'].apply(lambda x: 1 if x == 'Yes' else 0)
data['Polydipsia'] = data['Polydipsia'].apply(lambda x: 1 if x == 'Yes' else 0)
data['sudden weight loss'] = data['sudden weight loss'].apply(lambda x: 1 if x == 'Yes' else 0)
data['weakness'] = data['weakness'].apply(lambda x: 1 if x == 'Yes' else 0)
data['Polyphagia'] = data['Polyphagia'].apply(lambda x: 1 if x == 'Yes' else 0)
data['Genital thrush'] = data['Genital thrush'].apply(lambda x: 1 if x == 'Yes' else 0)
data['visual blurring'] = data['visual blurring'].apply(lambda x: 1 if x == 'Yes' else 0)
data['Itching'] = data['Itching'].apply(lambda x: 1 if x == 'Yes' else 0)
data['Irritability'] = data['Irritability'].apply(lambda x: 1 if x == 'Yes' else 0)
data['delayed healing'] = data['delayed healing'].apply(lambda x: 1 if x == 'Yes' else 0)
data['partial paresis'] = data['partial paresis'].apply(lambda x: 1 if x == 'Yes' else 0)
data['muscle stiffness'] = data['muscle stiffness'].apply(lambda x: 1 if x == 'Yes' else 0)
data['Alopecia'] = data['Alopecia'].apply(lambda x: 1 if x == 'Yes' else 0)
data['Obesity'] = data['Obesity'].apply(lambda x: 1 if x == 'Yes' else 0)

# Convert target variable to binary
data['class'] = data['class'].apply(lambda x: 1 if x == 'Positive' else 0)

# Save the converted data to a new file
data.to_csv('diabetes_data_upload_clean', index=False)
