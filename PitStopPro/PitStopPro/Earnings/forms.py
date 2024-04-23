from django import forms

class EarningsForm(forms.Form):
    num_months = forms.IntegerField(label='Number of Months', min_value=1, max_value=12)
    earnings_per_month = forms.DecimalField(label='Earnings per Month', max_digits=10, decimal_places=2)
