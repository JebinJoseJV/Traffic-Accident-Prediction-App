# Traffic-Accident-Prediction-App



[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-green)](https://traffic-accident-prediction-app-dqlpexy44xyfgkeylpgb6v.streamlit.app/)

This project is a **Machine Learning-based Traffic Accident Prediction App** that helps predict the severity of a traffic accident based on various input factors. The app is built using **Streamlit** for the frontend and **Scikit-Learn** for model training.

## 🚀 Live Demo
🔗 **Try the app here:**  
[Traffic Accident Prediction App](https://traffic-accident-prediction-app-dqlpexy44xyfgkeylpgb6v.streamlit.app/)

---

## 📌 Project Overview
- **Dataset:** Kaggle traffic accident dataset (processed for training).
- **Machine Learning Models Used:**
  - Logistic Regression
  - Decision Tree Classifier
  - Random Forest Classifier
  - Gradient Boosting Classifier
  - Multi-Layer Perceptron (MLP)
- **Best Model:** The best-performing model is automatically selected and used in the app.
- **Deployment:** The app is deployed on **Streamlit Cloud**.

---

## 🛠️ Features
✅ Predicts whether a traffic accident will be **Severe** or **Minor**  
✅ Uses pre-trained **Machine Learning models**  
✅ **No CSV file dependency** (Encoders & trained model are stored as `.pkl` files)  
✅ Interactive **user input form** for prediction  

---

## 📂 Project Structure

📦 Traffic-Accident-Prediction ├── 📜 README.md # Project documentation ├── 📜 app.py # Streamlit frontend for prediction ├── 📜 model_training.py # Model training and preprocessing ├── 📜 requirements.txt # Dependencies for the project ├── 📦 models/ # Folder for trained models │ ├── best_model.pkl # Best trained model (used in app) │ ├── label_encoders.pkl # Encoders for categorical features │ ├── feature_names.pkl # List of feature names

yaml
Copy
Edit

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/Traffic-Accident-Prediction.git
cd Traffic-Accident-Prediction
2️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the App Locally
sh
Copy
Edit
streamlit run app.py
🏗️ Model Training (Optional)
If you want to retrain the model, run:

sh
Copy
Edit
python model_training.py
This will train models, save the best one, and store the encoders and feature names.

📌 Technologies Used
Python 🐍
Streamlit (Web App)
Scikit-Learn (Machine Learning)
Pandas & NumPy (Data Processing)
Pickle (Model Serialization)
✨ Future Improvements
🚀 Add more features to improve accuracy
🚀 Implement additional ML models like XGBoost
🚀 Enhance UI with better visualization

📝 License
This project is open-source and available under the MIT License.
