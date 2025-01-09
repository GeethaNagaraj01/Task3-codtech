Name: Geetha N 
Company:CODETECH IT SOLUTIONS 
ID:CT0806EK 
Domain: DATA SCIENCE 
Duration:December 12th,2024 to january 12th,2025 
Mentor: Neha

OVERVIEW OF THE PROJECT

DATA PIPELINE DEVELOPMENT

This project involves building an ETL (Extract, Transform, Load) pipeline for data preprocessing, which includes handling missing data, encoding categorical variables, scaling numeric data, and splitting the data for machine learning model training. The pipeline uses pandas for data manipulation, scikit-learn for machine learning tasks like encoding and scaling, and is designed to process a dataset consisting of employee-related data.

The dataset includes the following columns:

Name: Name of the employee (String)
Age: Age of the employee (Numeric)
Salary: Salary of the employee (Numeric)
Department: Department where the employee works (Categorical: e.g., Sales, Marketing, Engineering)
Experience: Years of experience (Numeric)
City: City where the employee is based (Categorical)
The goal of the ETL pipeline is to:

Extract data from a CSV file.
Transform the data by:
Handling missing values (imputation for numerical and categorical columns).
Encoding categorical columns (such as Department and City) into numerical representations for machine learning compatibility.
Scaling numerical columns (such as Age, Salary, and Experience) to ensure they are on the same scale for machine learning models.
Splitting the dataset into features (X) and target variable (y), which is then divided into training and testing sets.
Load the transformed data into a new CSV file for later use in machine learning tasks or analysis.
Steps Involved in the Pipeline:
Loading the Data:

The dataset is loaded from a CSV file using pandas read_csv().
The dataset may contain missing values, which need to be handled during the transformation process.
Data Cleaning:

Missing Values: Numeric columns like Age, Salary, and Experience are filled with the mean of the column. Categorical columns like Department and City are filled with the placeholder 'Unknown'.
Data Preprocessing:

Categorical Encoding: Non-numeric columns (e.g., Department and City) are encoded into numerical labels using LabelEncoder from scikit-learn. For example, "Sales" becomes 0, "Marketing" becomes 1, etc.
Scaling: Numeric columns (e.g., Age, Salary, Experience) are scaled using StandardScaler, ensuring that all numeric features are on a similar scale, which helps improve the performance of machine learning models.
Data Splitting:

The data is divided into two parts: features (X) and the target variable (y). The target variable could be a column like Salary that you want to predict.
The data is split into training and testing sets, with 80% of the data used for training and 20% for testing. This split allows the model to be trained on one portion and validated on another portion.
Saving the Transformed Data:

The final transformed dataset is saved into a new CSV file, which can be used for further analysis or model training.
Output of the Pipeline:
Transformed Data: A new CSV file with the cleaned, encoded, and scaled data.
Train-Test Split: The data is split into training and testing sets, ready for use in machine learning algorithms.
Example Use Cases:
Predicting Salary: Using columns like Age, Department, Experience, and City, a model could be trained to predict an employee's Salary.
Classification Tasks: If you're predicting a categorical variable (e.g., which department an employee belongs to), the pipeline can be adapted for classification tasks.
Technologies Used:
pandas: For data manipulation and handling missing values.
scikit-learn: For encoding categorical variables and scaling numerical features.
Python: For orchestrating the ETL pipeline


![image](https://github.com/user-attachments/assets/3bdb699d-3387-4c87-bb06-9946c0311f65)

![image](https://github.com/user-attachments/assets/5154cc13-3a5d-4175-95d7-71a04e6d0996)

![image](https://github.com/user-attachments/assets/f797265a-6409-4f1c-a6aa-c8e18844b23d)




