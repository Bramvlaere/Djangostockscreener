from email import header
from django import urls
from django.http import response
import requests

headers={
    'Content-Type':'application/json',
    'Authorization': 'Token 9a719a868b9b757c64833606ee4e8053e7e616ea'
}

def get_meta_data(ticker):
    url='https://api.tiingo.com/tiingo/daily/{}'.format(ticker)
    response=requests.get(url,headers=headers)
    return response.json()

def get_price_data(ticker):
    url='https://api.tiingo.com/tiingo/daily/{}/prices'.format(ticker)
    response=requests.get(url,headers=headers)
    return response.json()[0]