
🌾 **Crop Recommendation System**

A machine learning project to predict the most suitable crop for cultivation based on soil and environmental conditions using Gradient Boosting.

🔍 **Overview**

This project builds a crop recommendation/prediction model that helps farmers and agricultural planners choose the best crop for a given set of conditions.
It uses Gradient Boosting, a powerful ensemble learning technique, to achieve high prediction accuracy.

📊 **Dataset
Source**: https://github.com/Anish-Das2003/Crop-Recommendation-System/blob/63128c76d026b39491af9e9c113b6e6c1021d79f/Crop_recommendation%20(1).csv

**Features**:

N – Nitrogen content in soil

P – Phosphorus content in soil

K – Potassium content in soil

temperature – Temperature (°C)

humidity – Relative humidity (%)

ph – Soil pH value

rainfall – Rainfall (mm)

Target:

label – Crop name (e.g., rice, wheat, maize, cotton, etc.)

⚙️ **Steps
Data loading and exploration**

Data cleaning and validation

Feature scaling (if required)

Train-test split

Model training using Gradient Boosting Classifier

Model evaluation using accuracy and classification metrics

Crop prediction for new input data

🧠 **Model Used** – Gradient Boosting
Ensemble learning technique that combines multiple weak learners

Builds models sequentially to correct previous errors

Handles non-linear relationships effectively

Reduces bias and variance, leading to better generalization

🛠️ **Tools Used**

Python,

Pandas, NumPy,

Scikit-learn,

Matplotlib, Seaborn,

Jupyter Notebook

📈 **Model Evaluation**

Accuracy Score,

Precision, 

Recall, 

F1-score,

Confusion Matrix

✅ **Results**

Achieved accuracy of ~99-100%

Model predicts crops reliably for unseen soil and climate data

Performs well across multiple crop classes
![image alt](https://github.com/Anish-Das2003/Crop-Recommendation-System/blob/aa36b5a60a93b11e786a9558f7212462d2456d97/Crop%20Recommendation.png)
![image alt](https://github.com/Anish-Das2003/Crop-Recommendation-System/blob/801afe1154aa6dc0fbddebe0de2686d4074b8ef1/Crop%20Recommendation1.png)


🌱 **Use Case**

Helps farmers select the most suitable crop

Supports smart agriculture and decision-making

Can be integrated into web or mobile applications
