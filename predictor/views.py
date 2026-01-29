from django.shortcuts import render
import pandas as pd

from .forms import CarPriceForm
from .ml.load_model import model, scaler, features


def predict_price(request):
    predicted_price = None

    if request.method == "POST":
        form = CarPriceForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            # Convert to DataFrame
            input_df = pd.DataFrame([data])

            # One-hot encoding
            input_df = pd.get_dummies(input_df)

            # Align with training columns
            input_df = input_df.reindex(columns=features, fill_value=0)

            # Scale using SAME scaler
            input_scaled = scaler.transform(input_df)

            # Predict
            predicted_price = model.predict(input_scaled)[0]

    else:
        form = CarPriceForm()

    return render(request, "predictor/predict.html", {
        "form": form,
        "price": predicted_price
    })
