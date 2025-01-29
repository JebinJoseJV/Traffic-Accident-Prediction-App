import streamlit as st
import pickle
import pandas as pd

def load_model():
    with open("best_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

with open("feature_names.pkl", "rb") as f:
    trained_feature_names = pickle.load(f)

categorical_cols = label_encoders.keys()

def preprocess_input(data):
    for column in categorical_cols:
        if column in data:
            data[column] = label_encoders[column].transform([data[column]])[0]

    data = {col: data[col] if col in data else 0 for col in trained_feature_names}
    return pd.DataFrame([data])

def main():
    st.title("Traffic Accident Prediction App")

    input_data = {}
    for col in trained_feature_names:
        if col in categorical_cols:
            input_data[col] = st.selectbox(f"{col}", label_encoders[col].classes_)
        else:
            input_data[col] = st.number_input(f"{col}", value=0, step=1)

    if st.button("Predict"):  
        input_df = preprocess_input(input_data)
        prediction = model.predict(input_df)[0]
        severity = "Accident is Severe" if prediction == 1 else "Accident is Minor"
        st.write(f"{severity}")

if __name__ == "__main__":
    main()
