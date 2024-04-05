# Cannabis Research Framework

This Python framework model is designed to handle various aspects of cannabis research, including data preprocessing, dimensionality reduction, clustering, regression, classification, SVM modeling, and evaluation metrics. It provides a structured approach to analyzing cannabis-related data and developing predictive models for research purposes.

## Usage

To use this framework, follow these steps:

1. Replace `'target_column'` with the actual target column name in your dataset.
2. Replace `'cannabis_data.csv'` with the path to your dataset.

## Features

### Data Preprocessing

The framework preprocesses the data by splitting it into training and testing sets, scaling features using StandardScaler, and encoding categorical variables if necessary.

### Dimensionality Reduction (PCA)

Principal Component Analysis (PCA) is applied to reduce the dimensionality of the data while preserving its variance. The number of principal components can be specified as a parameter.

### Clustering (KMeans)

The framework utilizes KMeans clustering to group similar data points together. The number of clusters can be specified as a parameter.

### Regression (Linear Regression)

Linear Regression is employed to build predictive models for continuous target variables. The framework fits a linear regression model to the training data.

### Classification (Random Forest)

Random Forest Classifier is used for building predictive models for categorical target variables. The framework trains a Random Forest model on the training data.

### SVM Model (GridSearchCV)

Support Vector Machine (SVM) model is trained using GridSearchCV for hyperparameter tuning. The framework performs a grid search over specified parameter values to find the best SVM model.

### Evaluation Metrics

The framework evaluates the performance of regression models using mean squared error (MSE) and classification models using accuracy score and classification report.

## Example Usage

```python
if __name__ == "__main__":
    data_path = 'cannabis_data.csv'
    framework = CannabisResearchFramework(data_path)
    results = framework.execute_framework()
    print(results)


Certainly! Below is the formatted README.md file for your GitHub repository:

markdown
Copy code
# Cannabis Research Framework

This Python framework model is designed to handle various aspects of cannabis research, including data preprocessing, dimensionality reduction, clustering, regression, classification, SVM modeling, and evaluation metrics. It provides a structured approach to analyzing cannabis-related data and developing predictive models for research purposes.

## Usage

To use this framework, follow these steps:

1. Replace `'target_column'` with the actual target column name in your dataset.
2. Replace `'cannabis_data.csv'` with the path to your dataset.

## Features

### Data Preprocessing

The framework preprocesses the data by splitting it into training and testing sets, scaling features using StandardScaler, and encoding categorical variables if necessary.

### Dimensionality Reduction (PCA)

Principal Component Analysis (PCA) is applied to reduce the dimensionality of the data while preserving its variance. The number of principal components can be specified as a parameter.

### Clustering (KMeans)

The framework utilizes KMeans clustering to group similar data points together. The number of clusters can be specified as a parameter.

### Regression (Linear Regression)

Linear Regression is employed to build predictive models for continuous target variables. The framework fits a linear regression model to the training data.

### Classification (Random Forest)

Random Forest Classifier is used for building predictive models for categorical target variables. The framework trains a Random Forest model on the training data.

### SVM Model (GridSearchCV)

Support Vector Machine (SVM) model is trained using GridSearchCV for hyperparameter tuning. The framework performs a grid search over specified parameter values to find the best SVM model.

### Evaluation Metrics

The framework evaluates the performance of regression models using mean squared error (MSE) and classification models using accuracy score and classification report.

## Example Usage

```python
if __name__ == "__main__":
    data_path = 'cannabis_data.csv'
    framework = CannabisResearchFramework(data_path)
    results = framework.execute_framework()
    print(results)
```
# Synthetic Cannabis Dataset Generator

This Python script generates a synthetic dataset for cannabis research purposes. It creates data with features such as THC content, CBD content, and terpene profiles, along with a binary target variable indicating the effectiveness of cannabis strains. Users can modify the parameters and features according to their specific requirements.

## Usage

To generate a synthetic dataset, follow these steps:

1. Adjust the parameters and features in the script according to your requirements.
2. Run the script to generate the synthetic dataset.
3. Once the CSV file is generated, you can use it with the framework model provided earlier.

## Features

### Synthetic Data Generation

The script generates synthetic data with the following features:

- THC content: Randomly generated values within a specified range.
- CBD content: Randomly generated values within a specified range.
- Terpene profiles: Randomly generated values for multiple terpenes.
- Effectiveness: Binary variable indicating the effectiveness of cannabis strains (0 or 1).

### Customization

Users can customize the following parameters and features:

- Number of samples: Adjust the number of samples in the dataset.
- Range of THC and CBD content: Define the range of THC and CBD content values.
- Number of terpenes: Specify the number of terpenes and their profiles.

## Example Usage

```python
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
num_samples = 1000

# Features
THC_content = np.random.uniform(0, 30, num_samples)
CBD_content = np.random.uniform(0, 30, num_samples)
terpene_profile = np.random.uniform(0, 1, (num_samples, 5))  # Assuming 5 different terpenes

# Target variable
effectiveness = np.random.randint(0, 2, num_samples)  # Binary variable indicating effectiveness (0 or 1)

# Create DataFrame
data = pd.DataFrame({
    'THC_content': THC_content,
    'CBD_content': CBD_content,
    'Terpene_1': terpene_profile[:, 0],
    'Terpene_2': terpene_profile[:, 1],
    'Terpene_3': terpene_profile[:, 2],
    'Terpene_4': terpene_profile[:, 3],
    'Terpene_5': terpene_profile[:, 4],
    'Effectiveness': effectiveness
})

# Save DataFrame to CSV
data.to_csv('cannabis_data.csv', index=False)
```

## Requirements

Python 3.x,
pandas,
numpy,
scikit-learn

## License
This script is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.
