from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model and preprocessor
model = joblib.load("data/best_churn_model.pkl")
preprocessor = joblib.load("data/preprocessor.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    probability = None

    if request.method == "POST":

        customer_data = {
            "gender": request.form["gender"],
            "SeniorCitizen": int(request.form["SeniorCitizen"]),
            "Partner": request.form["Partner"],
            "Dependents": request.form["Dependents"],
            "tenure": int(request.form["tenure"]),
            "PhoneService": request.form["PhoneService"],
            "MultipleLines": request.form["MultipleLines"],
            "InternetService": request.form["InternetService"],
            "OnlineSecurity": request.form["OnlineSecurity"],
            "OnlineBackup": request.form["OnlineBackup"],
            "DeviceProtection": request.form["DeviceProtection"],
            "TechSupport": request.form["TechSupport"],
            "StreamingTV": request.form["StreamingTV"],
            "StreamingMovies": request.form["StreamingMovies"],
            "Contract": request.form["Contract"],
            "PaperlessBilling": request.form["PaperlessBilling"],
            "PaymentMethod": request.form["PaymentMethod"],
            "MonthlyCharges": float(request.form["MonthlyCharges"]),
            "TotalCharges": float(request.form["TotalCharges"]),
            "numAdminTickets": int(request.form["numAdminTickets"]),
            "numTechTickets": int(request.form["numTechTickets"])
        }

        # Convert input into DataFrame
        input_df = pd.DataFrame([customer_data])

        # Transform input using the same preprocessor used during training
        input_processed = preprocessor.transform(input_df)

        # Make prediction
        prediction_result = model.predict(input_processed)[0]
        probability_result = model.predict_proba(input_processed)[0][1]

        prediction = "Yes" if prediction_result == 1 else "No"
        probability = round(probability_result * 100, 2)

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability
    )


if __name__ == "__main__":
    app.run(debug=False)