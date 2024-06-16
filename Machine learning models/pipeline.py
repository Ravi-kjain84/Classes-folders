from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

# Load the digits dataset
digits = load_digits()
X = digits.data
y = digits.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a pipeline with preprocessing steps
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=10)),
    ('classifier', RandomForestClassifier())  # Placeholder, will be replaced by GridSearchCV
])

# Define the parameter grid to search over
param_grid = [
    {'classifier': [RandomForestClassifier()], 'classifier__n_estimators': [100, 200]},
    {'classifier': [LogisticRegression(max_iter=1000)], 'classifier__C': [0.1, 1, 10]},  # Increased max_iter
    {'classifier': [SVC(max_iter=1000)], 'classifier__C': [0.1, 1, 10]}  # Increased max_iter, if necessary
]

# Set up GridSearchCV to find the best classifier
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Print the best parameters and the best score
print("Best parameters:", grid_search.best_params_)
print("Best score:", grid_search.best_score_)

# Predict on test data with the best found model
y_pred = grid_search.predict(X_test)

# Evaluate the results
from sklearn.metrics import accuracy_score
print("Test set accuracy:", accuracy_score(y_test, y_pred))