from requests import request, codes
import json
from datetime import datetime
from config_data.config import API_KEY, PRICE_URL, LIST_URL
from loader import cache


class Currency:

    _headers = {"apikey": API_KEY}

    @staticmethod
    def get_price(base: str, quote: str, amount: int) -> float:
        params = {"from": base, "to": quote, "amount": amount}
        response = request("GET", PRICE_URL, headers = Currency._headers, params = params)
        if response.status_code == codes.ok:
            result = json.loads(response.text)
            price = result.get("result")
            Currency.to_cache(base, quote, amount, price)
            return price
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

    @staticmethod
    def try_from_cache(base: str, quote: str, amount: int) -> float:
        data = cache.get("{}-{}".format(base, quote))
        price = 0
        if data:
            dt_now = datetime.now()
            dt = data[0]
            delta = (dt_now - dt).seconds / 3600
            if delta < 1:
                price = round(data[1] * amount, 4)
        return price

    @staticmethod
    def to_cache(base: str, quote: str, amount: int, price: float):
        cost_one = round(price / amount, 4)
        dt = datetime.now()
        cache["{}-{}".format(base, quote)] = (dt, cost_one)
