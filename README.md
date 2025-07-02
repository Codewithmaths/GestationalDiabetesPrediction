# 🤰 Gestational Diabetes Prediction with Streamlit UI
This project leverages machine learning and an intuitive Streamlit-based user interface to predict the risk of Gestational Diabetes Mellitus (GDM) in pregnant women. Designed to be both accurate and user-friendly, it enables early risk assessment using basic health parameters.

🎯 Objective
To build an interactive tool that predicts the likelihood of developing gestational diabetes using maternal data, assisting healthcare providers in taking preventive measures early in the pregnancy.

🚀 Key Features
🧠 Machine Learning Model trained on real-world healthcare data
📊 Interactive Streamlit Web App for real-time prediction
🔍 Exploratory Data Analysis (EDA) and visual insights
📈 Model Performance Evaluation with accuracy, precision, recall, and F1-score
📥 User Input Form to enter pregnancy-related details for prediction
💾 Optionally integrates with database to store predictions (optional feature)
🧪 Tech Stack
Python
Pandas, NumPy – Data preprocessing
Scikit-learn – ML model training (e.g., Random Forest, Logistic Regression)
Matplotlib, Seaborn – Visualization
Streamlit – Web application development
Pickle/Joblib – Model serialization
📁 Folder Structure
├── data/                 # Raw and cleaned datasets
├── app/                  # Streamlit UI files
├── models/               # Trained machine learning models
├── images/               # Plots and visuals
├── notebooks/            # EDA and model training notebooks
├── requirements.txt      # Required libraries
├── main.py               # Main Streamlit app
└── README.md             # Project overview
💡 How to Run the Project
Clone the repository:

git clone https://github.com/your-username/gestational-diabetes-prediction.git
cd gestational-diabetes-prediction
Install dependencies:

pip install -r requirements.txt
Run the Streamlit app:

streamlit run main.py
📈 Results
The Random Forest model achieved ~XX% accuracy (replace with your metric) and showed significant performance in identifying high-risk cases. Feature analysis highlighted the importance of glucose levels, BMI, age, and blood pressure.

🔮 Future Enhancements
Deploy the app on Streamlit Cloud / Heroku / AWS
Add user authentication for secure access
Enhance UI/UX with additional visualizations
Connect to a cloud-based database for prediction history
