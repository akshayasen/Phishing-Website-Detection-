import joblib
import re
import pandas as pd
from urllib.parse import urlparse
import streamlit as st

# Load the trained Random Forest model
model = joblib.load("rf_model_refined.pkl")

# Function to extract features from a URL
def extract_features_from_url(url):
    parsed = urlparse(url)
    hostname = parsed.hostname or ''
    path = parsed.path or ''

    length_url = len(url)
    length_hostname = len(hostname)
    num_special_chars = len(re.findall(r'[^\w\s]', url))
    num_digits = sum(c.isdigit() for c in url)
    subdomain_count = hostname.count('.') - 1 if hostname else 0
    domain_age = -1 
    web_traffic = 0  
    page_rank = 0    
    google_index = 1 if "google" in url else 0  

    # Create a DataFrame with extracted features
    features = pd.DataFrame([[
        length_url, length_hostname, num_special_chars, num_digits,
        subdomain_count, domain_age, web_traffic, page_rank, google_index
    ]], columns=[
        'length_url', 'length_hostname', 'num_special_chars', 'num_digits',
        'subdomain_count', 'domain_age', 'web_traffic', 'page_rank', 'google_index'
    ])
    
    return features

# Streamlit App UI
st.title("🔐 Phishing Website Detector")
st.markdown("Enter a website URL and detect whether it is **Legitimate** or **Phishing**.")

user_url = st.text_input("Enter URL:", placeholder="https://example.com")

if st.button("Detect"):
    if user_url:
        try:
            input_data = extract_features_from_url(user_url)
            prediction = model.predict(input_data)[0]

            if prediction == 0:
                st.success("✅ This website is **Likely Legitimate**.")
            else:
                st.error("⚠️ Warning! This website is **Likely Phishing**.")
        except Exception as e:
            st.error(f"Error during prediction: {e}")
    else:
        st.warning("Please enter a URL.") 
