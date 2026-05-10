# 🔊 SONAR Mine vs Rock Prediction

A Machine Learning web app that predicts whether an underwater object is a **Mine** or a **Rock** based on SONAR signal data.

---

## 📌 About the Project

This is my first Machine Learning project. It uses the SONAR dataset which contains 60 sonar frequency readings. The model is trained to classify the object as either a Mine (M) or a Rock (R).

---

## 🤖 Model Used

- **Algorithm:** Logistic Regression
- **Library:** Scikit-learn
- **Accuracy:** ~83% on test data

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- NumPy
- Pandas
- Streamlit (for UI)

---

## 🚀 How to Run Locally

1. Clone the repository
   ```
   git clone https://github.com/mohammedjunaidahmed-dev/Sonar-Project.git
   ```

2. Navigate to the project folder
   ```
   cd Sonar-Project
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Run the app
   ```
   python -m streamlit run app.py
   ```

5. Open your browser and go to
   ```
   http://localhost:8501
   ```

---

## 💡 How to Use

- Paste 60 comma-separated sonar signal values into the input box
- Click the **Predict** button
- The app will tell you if the object is a **Mine 💣** or a **Rock 🪨**

---

## 📂 Project Structure

```
Sonar-Project/
├── app.py               # Streamlit web app
├── sonar_model.pkl      # Trained Logistic Regression model
├── requirements.txt     # Required libraries
└── README.md            # Project documentation
```

---

## 📚 Dataset

* You can download the dataset from Kaggle
* The dataset contains 208 samples with 60 features each
* Each feature represents the energy of a sonar signal at a specific frequency

---

## 👨‍💻 Author

**Mohammed Junaid Ahmed**
- GitHub: [@mohammedjunaidahmed-dev](https://github.com/mohammedjunaidahmed-dev)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).