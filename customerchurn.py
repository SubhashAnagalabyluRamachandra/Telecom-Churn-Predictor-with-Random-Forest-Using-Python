# Customer Churn Analysis
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from IPython.display import display
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns

train_path = "/content/train.csv"
test_path = "/content/test.csv"

train_data = pd.read_csv(train_path)
test_data = pd.read_csv(test_path)
train_data.head()  # View the first few rows of the training data
train_data.info()  # Get information about the training data (e.g., data types, missing values)

# Preprocess the data
label_encoder = LabelEncoder()
categorical_columns = ["state", "area_code", "international_plan", "voice_mail_plan"]

for column in categorical_columns:
    train_data[column] = label_encoder.fit_transform(train_data[column])
    test_data[column] = label_encoder.transform(test_data[column])

# Split the data into input features (X) and the target variable (y)
X = train_data.drop("churn", axis=1)
y = train_data["churn"]

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions on the test set (excluding the "id" column)
test_data_predictions = model.predict(test_data.drop("id", axis=1))

# Create a DataFrame with the test predictions (including the "id" column)
submission_df = pd.DataFrame({"id": test_data["id"], "churn": test_data_predictions})
display(submission_df)

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
val_predictions = model.predict(X_val)
accuracy = accuracy_score(y_val, val_predictions)
precision = precision_score(y_val, val_predictions, pos_label='yes')
recall = recall_score(y_val, val_predictions, pos_label='yes')
confusion_mat = confusion_matrix(y_val, val_predictions)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("Confusion Matrix:")
print(confusion_mat)

# Perform cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)

# Print the cross-validation scores
print("Cross-Validation Scores:", cv_scores)
print("Average Cross-Validation Score:", cv_scores.mean())

# Confusion Matrix
sns.set(font_scale=1.2)
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_mat, annot=True, cmap='Blues', fmt='g', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Bar Plot for Cross-Validation Scores
plt.figure(figsize=(8, 6))
sns.barplot(x=[1, 2, 3, 4, 5], y=cv_scores, color='skyblue')
plt.title('Cross-Validation Scores')
plt.xlabel('Fold')
plt.ylabel('Score')
plt.ylim(0.9, 1.0)  # Set the y-axis limits for better visualization
plt.show()
