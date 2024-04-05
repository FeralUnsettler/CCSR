import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

class CannabisResearchFramework:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        
    def preprocess_data(self):
        # Data preprocessing steps
        X = self.data.drop(columns=['target_column'])
        y = self.data['target_column']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        return X_train_scaled, X_test_scaled, y_train, y_test
    
    def dimensionality_reduction(self, X_train, X_test, n_components):
        # Dimensionality reduction using PCA
        pca = PCA(n_components=n_components)
        X_train_pca = pca.fit_transform(X_train)
        X_test_pca = pca.transform(X_test)
        return X_train_pca, X_test_pca
    
    def clustering(self, X_train, n_clusters):
        # Clustering using KMeans
        kmeans = KMeans(n_clusters=n_clusters)
        clusters = kmeans.fit_predict(X_train)
        return clusters
    
    def regression_model(self, X_train, y_train):
        # Regression model using Linear Regression
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    
    def classification_model(self, X_train, X_test, y_train, y_test):
        # Classification model using Random Forest
        clf = RandomForestClassifier()
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        return clf, accuracy, report
    
    def svm_model(self, X_train, y_train):
        # SVM model using GridSearchCV
        param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001], 'kernel': ['rbf', 'poly', 'sigmoid']}
        svm = SVC()
        grid = GridSearchCV(svm, param_grid, refit=True, verbose=3)
        grid.fit(X_train, y_train)
        return grid.best_estimator_
    
    def evaluate_regression_model(self, model, X_test, y_test):
        # Evaluate regression model
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        return mse
    
    def execute_framework(self):
        X_train, X_test, y_train, y_test = self.preprocess_data()
        X_train_pca, X_test_pca = self.dimensionality_reduction(X_train, X_test, n_components=10)
        clusters = self.clustering(X_train_pca, n_clusters=5)
        regression_model = self.regression_model(X_train, y_train)
        classification_model, accuracy, report = self.classification_model(X_train, X_test, y_train, y_test)
        svm_model = self.svm_model(X_train, y_train)
        mse = self.evaluate_regression_model(regression_model, X_test, y_test)
        
        return {
            'clusters': clusters,
            'regression_model': regression_model,
            'classification_model': classification_model,
            'svm_model': svm_model,
            'accuracy': accuracy,
            'classification_report': report,
            'mse': mse
        }

# Example usage:
if __name__ == "__main__":
    data_path = 'cannabis_data.csv'
    framework = CannabisResearchFramework(data_path)
    results = framework.execute_framework()
    print(results)
