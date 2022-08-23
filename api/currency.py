from requests import request, codes
import json
from config_data.config import API_KEY, PRICE_URL, LIST_URL


class Currency:

    _headers = {"apikey": API_KEY}

    @staticmethod
    def get_price(base: str, quote: str, amount: int) -> float:
        params = {"from": base, "to": quote, "amount": amount}
        response = request("GET", PRICE_URL, headers = Currency._headers, params = params)
        if response.status_code == codes.ok:
            result = json.loads(response.text)
            return result.get("result")
        else:
            return 0

    @staticmethod
    def get_list() -> dict:
        response = request("GET", LIST_URL, headers=Currency._headers)
        if response.status_code == codes.ok:
            result = json.loads(response.text)
            return result.get("currencies")
        else:
            return {}

