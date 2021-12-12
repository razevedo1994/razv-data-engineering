from requests import request
from extracting_data_from_api.setup.settings import API_KEY
import json

base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
params = {"start": "1", "limit": "5000", "convert": "USD"}

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY,
}

response = request.get(base_url, params=params)
