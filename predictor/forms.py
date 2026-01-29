from django import forms
class CarPriceForm(forms.Form):

    year = forms.IntegerField()
    mileage = forms.IntegerField()
    tax = forms.FloatField()
    mpg = forms.FloatField()
    engineSize = forms.FloatField()

    fuelType = forms.ChoiceField(choices=[
        ("Petrol", "Petrol"),
        ("Diesel", "Diesel"),
        ("Hybrid", "Hybrid"),
        ("Electric", "Electric"),
    ])

    transmission = forms.ChoiceField(choices=[
        ("Manual", "Manual"),
        ("Automatic", "Automatic"),
        ("Semi-Auto", "Semi-Auto"),
    ])
    model = forms.CharField()
