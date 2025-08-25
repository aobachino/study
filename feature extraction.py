import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_selection import chi2
import numpy as np

# Load the dataset
data = pd.read_csv('Phishing_Email.csv')

# Function to clean email text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text) # Remove digits
    text = re.sub(r'https?://\S+|www\.\S+', '', text) # Remove URLs
    text = re.sub(r'<.*?>', '', text) # Remove HTML tags
    text = re.sub(r'[^\w\s]', '', text) # Remove punctuation
    return text

data['Email Text'] = data['Email Text'].apply(clean_text)

# Label Encoding
data['Email Type'] = data['Email Type'].apply(lambda x: 1 if x == 'Phishing Email' else 0)

# Feature Extraction
# Common phishing keywords
phishing_keywords = ['urgent', 'verify', 'account', 'password', 'login', 'click', 'update', 'security', 'alert', 'win', 'free', 'gift', 'suspended', 'unauthorized', 'immediate', 'attention']

def keyword_feature(text, keywords):
    return sum(1 for word in keywords if word in text)

data['Keyword Count'] = data['Email Text'].apply(lambda x: keyword_feature(x, phishing_keywords))

# Number of links
data['Num Links'] = data['Email Text'].apply(lambda x: len(re.findall(r'https?://\S+|www\.\S+', x)))

# Length of email
data['Email Length'] = data['Email Text'].apply(len)

# Vectorization
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X = vectorizer.fit_transform(data['Email Text'])

# Convert to DataFrame
features = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
features['Keyword Count'] = data['Keyword Count']
features['Num Links'] = data['Num Links']
features['Email Length'] = data['Email Length']
features['Email Type'] = data['Email Type']

# Feature Selection using Chi-square
X = features.drop(columns=['Email Type'])
y = features['Email Type']
chi2_scores, p_values = chi2(X, y)

# Create DataFrame of scores and p-values
chi2_df = pd.DataFrame({'Feature': X.columns, 'Chi2 Score': chi2_scores, 'p-value': p_values})
chi2_df = chi2_df.sort_values('Chi2 Score', ascending=False)

# Select top features
selected_features = chi2_df[chi2_df['p-value'] < 0.05]['Feature']

# Final DataFrame with selected features
final_features = features[selected_features]

# Save the processed data to a new CSV file
final_features.to_csv('processed_phishing_emails.csv', index=False)

print("Feature extraction and selection completed successfully!")
