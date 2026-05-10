import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("sonar_model.pkl", "rb"))

st.title("🔊 SONAR Mine vs Rock Detector")
st.write("Paste all 60 values separated by commas in the box below:")

user_input = st.text_area("Input Values", height=150)

if st.button("🔍 Predict"):
    try:
        values = [float(x.strip()) for x in user_input.split(",")]
        if len(values) != 60:
            st.warning(f"⚠️ You entered {len(values)} values. Please enter exactly 60.")
        else:
            data = np.array(values).reshape(1, -1)
            result = model.predict(data)[0]
            st.markdown("---")
            if result == "R":
                st.success("🪨 The object is a **ROCK**")
            else:
                st.error("💣 The object is a **MINE**")
    except:
        st.error("❌ Something went wrong. Make sure all values are numbers separated by commas.")