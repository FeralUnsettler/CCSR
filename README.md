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
