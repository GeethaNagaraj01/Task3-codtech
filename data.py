import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

def load_data(file_path: str):
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(f"Data loaded from {file_path}")
        print(f"Columns in the dataset: {df.columns}")
        return df
    else:
        raise FileNotFoundError(f"File not found: {file_path}")

def clean_data(df):

    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())


    non_numeric_cols = df.select_dtypes(exclude=['number']).columns
    df[non_numeric_cols] = df[non_numeric_cols].fillna('Unknown')

    print("Missing values handled")
    return df



def preprocess_data(df):
    categorical_cols = df.select_dtypes(include=['object']).columns

    label_encoder = LabelEncoder()
    for col in categorical_cols:
        df[col] = label_encoder.fit_transform(df[col])

    print("Categorical data encoded")
    return df


def scale_data(df):
    numeric_cols = df.select_dtypes(include=['number']).columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    print("Numerical data scaled")
    return df

def split_data(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Data split into training and testing (80/20 split)")
    return X_train, X_test, y_train, y_test

def save_data(df, output_path: str):
    df.to_csv(output_path, index=False)
    print(f"Transformed data saved to {output_path}")



def etl_pipeline(input_file, output_file, target_column):

    data = load_data(input_file)


    data_clean = clean_data(data)
    data_processed = preprocess_data(data_clean)
    data_scaled = scale_data(data_processed)


    X_train, X_test, y_train, y_test = split_data(data_scaled, target_column)

    # Load Data (Save Transformed Data to a CSV)
    save_data(data_scaled, output_file)
    print("ETL process completed successfully!")



input_file = '/home/gnagaraj/PycharmProjects/data pipeline/input_data.csv'
output_file = '/home/gnagaraj/PycharmProjects/data pipeline/output_transformed_data.csv'
target_column = 'Salary'
etl_pipeline(input_file, output_file, target_column)

