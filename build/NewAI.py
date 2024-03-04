import tkinter as tk
from tkinter import filedialog
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import pandas as pd
import pickle
from docx import Document

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load and preprocess dataset
dataset = pd.read_csv('C:\\Users\\USER\\Documents\\Projects\\Major Project\\Skive\\build\\assets\\even_more_expanded_corporate_problems_skills.csv')

# Preprocessing function
def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if not word in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    return ' '.join(tokens)

# Apply preprocessing to problem statements
dataset['processed_statement'] = dataset['problem_statement'].apply(preprocess_text)

# Vectorize problem statements using TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
X = tfidf_vectorizer.fit_transform(dataset['processed_statement'])
y = dataset['required_skills']

# Train Support Vector Machine (SVM) classifier
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X, y)

# Save the trained vectorizer
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf_vectorizer, f)

# Save the trained classifier
with open('classifier.pkl', 'wb') as f:
    pickle.dump(svm_classifier, f)

# Function to extract text from Word document
def extract_text_from_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Function to predict required skills
def predict_required_skills(problem_statement):
    processed_statement = preprocess_text(problem_statement)
    vectorized_statement = tfidf_vectorizer.transform([processed_statement])
    predicted_skills = svm_classifier.predict(vectorized_statement)
    return predicted_skills

# GUI application
def upload_document():
    file_path = filedialog.askopenfilename(filetypes=[("Word documents", "*.docx"), ("All files", "*.*")])
    if file_path:
        try:
            document_text = extract_text_from_docx(file_path)
            predicted_skills = predict_required_skills(document_text)
            result_label.config(text="Predicted required skills: " + str(predicted_skills))
        except Exception as e:
            result_label.config(text="Error occurred: " + str(e))

# Create GUI window
root = tk.Tk()
root.title("Skill Prediction Tool")

# Create and place widgets
upload_button = tk.Button(root, text="Upload Document", command=upload_document)
upload_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI application
root.mainloop()
