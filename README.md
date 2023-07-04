# Telecom-Churn-Predictor-with-Random-Forest-Using-Python
Telecom-Churn-Predictor: A Python project implementing a Random Forest model to predict customer churn in the telecommunications industry. It aims to predict whether customers of a telecommunications company will churn or not, helping the company proactively identify customers at risk of switching to another provider. The project utilizes a dataset containing various customer features such as state, account length, area code, international plan, voice mail plan, call details, and customer service calls. The workflow involves data preprocessing, including label encoding of categorical variables and splitting the data into training and validation sets. The Random Forest Classifier is then trained on the training data to learn patterns and make predictions. The model's performance is evaluated using accuracy, precision, recall, and a confusion matrix.

Additionally, cross-validation is performed to assess the model's generalization ability. The cross-validation scores are visualized using a bar plot to provide insights into the model's performance across different folds. This project serves as a practical application of machine learning techniques to solve the real-world problem of customer churn in the telecommunications industry. It showcases the use of Python, popular libraries like pandas, scikit-learn, and matplotlib, as well as data preprocessing, model training, evaluation, and visualization techniques.

Key Features
- Data preprocessing and encoding of categorical variables
- Splitting the data into training and validation sets
- Training a Random Forest classifier on the training data
- Evaluating the model's performance using accuracy, precision, recall, and confusion matrix
- Conducting cross-validation to assess model stability
- Visualization of the confusion matrix and cross-validation scores

Repository Structure
- test.csv: Contains the test dataset in CSV format
- train.csv: Contains the training dataset in CSV format
- CustomerChurn.ipynb: Notebooks with step-by-step code and analysis
- Result.csv: Outputs of the trained model, including predictions and evaluation metrics
- README.md: Overview of the project, instructions, and key information
