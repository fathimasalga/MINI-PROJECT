import streamlit as st
import pickle
import numpy as np

st.title("Dry Bean Classification")

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.subheader("Enter Feature Values")

# List of features
feature_names = [
    "Area", "Perimeter", "MajorAxisLength", "MinorAxisLength",
    "AspectRatio", "Eccentricity", "ConvexArea", "EquivDiameter",
    "Extent", "Solidity", "Roundness", "Compactness",
    "ShapeFactor1", "ShapeFactor2", "ShapeFactor3", "ShapeFactor4"
]

inputs = []
for feature in feature_names:
    val = st.number_input(feature, value=0.0)
    inputs.append(val)

if st.button("Predict"):
    X = np.array(inputs).reshape(1, -1)
    prediction = model.predict(X)
    st.success(f"Predicted Bean Class: {prediction[0]}")
