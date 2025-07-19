
from SmartApi import SmartConnect
import pyotp
import os

API_KEY = "xmsozBTs"
CLIENT_CODE = "AAAH458913"
SECRET_KEY = "0e453386-4fd0-4406-80e2-334169c5192b"
TOTP_SECRET = "G74DLD3L4JJ6J4TOCLGERJXX7M"

def place_order(decision):
    obj = SmartConnect(api_key=API_KEY)
    totp = pyotp.TOTP(TOTP_SECRET).now()
    data = obj.generateSession(CLIENT_CODE, SECRET_KEY, totp)

    try:
        order = obj.placeOrder(
            variety="NORMAL",
            tradingsymbol=f"{decision['symbol']}{decision['strike_price']}{decision['option_type'][0]}",
            symboltoken="99926009",  # replace with actual token
            transactiontype=decision["action"],
            exchange="NFO",
            ordertype="MARKET",
            producttype="INTRADAY",
            duration="DAY",
            quantity=50  # example
        )
        return order
    except Exception as e:
        return {"error": str(e)}
