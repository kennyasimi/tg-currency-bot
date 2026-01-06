
import requests
from bot.utils.logger import logger

class ExchangeService:
    def __init__(self):
        self.base_url = "https://api.frankfurter.app/latest"
        self.currencies_url = "https://api.frankfurter.app/currencies"
        self.supported_currencies = self._get_supported_currencies()

    def _get_supported_currencies(self):
        """Fetch the list of supported currency codes from the API"""
        try:
            response = requests.get(self.currencies_url)
            data = response.json()
            logger.info(f"Supported currencies loaded: {list(data.keys())}")
            return list(data.keys())
        except Exception as e:
            logger.error(f"Failed to fetch supported currencies: {e}")
            # fallback to common currencies
            return ["USD", "EUR", "GBP", "JPY", "INR", "CAD", "AUD", "CHF", "CNY"]

    def get_exchange_rate(self, from_currency: str, to_currency: str) -> tuple:
        """Get exchange rate from 'from_currency' to 'to_currency'"""
        from_code = from_currency.split(' ')[0].upper()
        to_code = to_currency.split(' ')[0].upper()

        # Check if currencies are supported
        if from_code not in self.supported_currencies:
            msg = f"Currency {from_code} not supported by the API"
            logger.warning(msg)
            return None, msg
        if to_code not in self.supported_currencies:
            msg = f"Currency {to_code} not supported by the API"
            logger.warning(msg)
            return None, msg

        try:
            logger.debug(f"Requesting exchange rate: {from_code} -> {to_code}")
            response = requests.get(f"{self.base_url}?from={from_code}&to={to_code}")
            data = response.json()
            logger.debug(f"API response data: {data}")

            if 'rates' in data and to_code in data['rates']:
                rate = data['rates'][to_code]
                logger.info(f"Exchange rate {from_code}->{to_code}: {rate}")
                return rate, None
            else:
                msg = f"Currency conversion failed: {from_code} -> {to_code}"
                logger.warning(msg)
                return None, msg
        except Exception as e:
            logger.error(f"API Error: {e}")
            return None, str(e)


