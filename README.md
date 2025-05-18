# Phishing-Website-Detection-

This project aims to detect phishing websites using machine learning techniques. Phishing websites are designed to mimic legitimate sites in order to steal sensitive information like usernames, passwords, and financial details. By analyzing various features extracted from URLs and domain metadata, this model helps distinguish between legitimate and phishing websites.

# Project Objective:

The main goal is to develop a binary classification model that predicts whether a website is phishing or legitimate based on features such as URL length, domain age, presence of IP addresses, and other structural characteristics. This helps users, cybersecurity teams, and automated systems make quick and accurate decisions to prevent cyber fraud.

# Key Highlights:

* Built using Random Forest Classifier
* Achieved an accuracy of 96%
* Provides a user-friendly interface where users can input a URL and get real-time predictions

# Dataset Overview
The dataset consists of URLs labeled as legitimate or phishing, along with over 80+ extracted features that help in identifying suspicious patterns. The dataset was cleaned, preprocessed, and used to train the model.

# Summary:
 
* Total Records: 11,000+ rows , 89 columns 
* Target Column: status → (phishing or legitimate)
* Class Distribution: Balanced (50% phishing, 50% legitimate)
* Duplicates: 0
* Missing/Invalid Values: Removed (including negative domain ages)

 # Key Features:
 
length_url, length_hostname, ip, nb_dots, nb_hyphens

domain_age, domain_registration_length, web_traffic

google_index, page_rank, dns_record, subdomain_count

… and many more URL- and domain-related indicators

# Model Used Algorithm:

* Random Forest Classifier

Reason for Choosing:

* Handles high-dimensional feature spaces well
* Works effectively with both categorical and numerical data
* Provides feature importance
* Robust to overfitting

#  Model Evaluation:

* Accuracy: 96%
* Precision / Recall / F1-score: Balanced and high

# Evaluation Tools:

* Confusion Matrix
* Classification Report


#  Project Workflow:

Data Preprocessing:

* Removed invalid entries (like negative domain ages)
* Handled missing values
* Normalized/Scaled features if necessary

Exploratory Data Analysis (EDA) :

* Visualized feature distributions
* Correlation heatmaps
* Identified key indicators of phishing behavior

Feature Engineering : 

* Selected relevant features
* Removed low-importance or noisy features

Model Building & Training : 

* Used GridSearchCV to tune hyperparameters
* Trained using Random Forest

Model Evaluation:

* Used metrics like Accuracy, F1-score
* Visual explanation with SHAP 


# Tools & Technologies Used: 

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Streamlit
* Joblib
* Jupyter Notebook

# Future Improvements: 

* Automate feature extraction from real-time URLs
* Integrate with web browsers for phishing detection
* Expand dataset with more diverse phishing examples
* Add real-time alerts or email notifications

