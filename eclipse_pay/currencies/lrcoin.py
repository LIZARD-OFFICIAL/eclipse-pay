from eclipse_pay import BaseCurrency
import requests
from warnings import warn

class LRCOIN(BaseCurrency):
    """LRCOIN API handler"""
    @property
    def name():
        return "lrcoin"
    @staticmethod
    def check_transaction(sender, recipient, amount) -> bool:
        response = requests.get(f"https://lrc-dxbt.onrender.com/check/{sender}/{recipient}/{amount}")
        if response == {"paid":"true"}:
            return True
        elif response == {"paid":"false"}:
            return False
        else:
            warn("API returned unexpected response. Check eclipse-pay version.",RuntimeWarning) # unstable render free plan goes brrrr
            return False