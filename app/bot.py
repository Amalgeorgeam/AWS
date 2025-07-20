
import time
import pyotp
from SmartApi.smartConnect import SmartConnect
from config.settings import API_KEY, CLIENT_ID, CLIENT_SECRET, TOTP_SECRET

def generate_session():
    totp = pyotp.TOTP(TOTP_SECRET)
    otp = totp.now()
    obj = SmartConnect(api_key=API_KEY)
    session_data = obj.generateSession(CLIENT_ID, CLIENT_SECRET, otp)
    return obj, session_data

def get_ltp(obj, token="3045", exchange="NSE", symbol="RELIANCE"):
    return obj.ltpData(exchange=exchange, tradingsymbol=symbol, symboltoken=token)

def place_order(obj, symbol="RELIANCE", token="3045"):
    order = obj.placeOrder(
        variety="NORMAL",
        tradingsymbol=symbol,
        symboltoken=token,
        transactiontype="BUY",
        exchange="NSE",
        ordertype="MARKET",
        producttype="INTRADAY",
        duration="DAY",
        price="0",
        squareoff="0",
        stoploss="0",
        quantity="1"
    )
    return order

def main_trading_logic():
    obj, session = generate_session()
    ltp_data = get_ltp(obj)
    print("LTP:", ltp_data["data"]["ltp"])
    if ltp_data["data"]["ltp"] < 3000:
        print("Placing order...")
        result = place_order(obj)
        return result
    return {"message": "No action taken"}
