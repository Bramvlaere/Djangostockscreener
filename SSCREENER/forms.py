from operator import length_hint
from django import forms

class TickerForm(forms.Form):
    ticker=forms.CharField(label='Ticker',max_length=5)