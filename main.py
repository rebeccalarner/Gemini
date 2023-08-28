import requests
import json
import sqlite3


def create_database():
    conn = sqlite3.connect("gemini_data.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ticker (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        base_currency TEXT,
        quote_currency TEXT,
        bid REAL,
        ask REAL,
        last REAL,
        f_upload_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS OrderBook (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        base_currency TEXT,
        quote_currency TEXT,
        type TEXT,
        price REAL,
        amount REAL,
        f_upload_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS TradeHistory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        base_currency TEXT,
        quote_currency TEXT,
        timestamp INTEGER,
        price REAL,
        amount REAL,
        f_upload_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );""")

    conn.commit()
    conn.close()


def fetch_ticker(base_currency='btc', quote_currency='usd'):
    endpoint = f"https://api.gemini.com/v1/pubticker/{base_currency}{quote_currency}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return f"Error: {response.status_code}"


def fetch_order_book(base_currency='btc', quote_currency='usd'):
    endpoint = f"https://api.gemini.com/v1/book/{base_currency}{quote_currency}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return f"Error: {response.status_code}"


def fetch_trade_history(base_currency='btc', quote_currency='usd'):
    endpoint = f"https://api.gemini.com/v1/trades/{base_currency}{quote_currency}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return f"Error: {response.status_code}"


def save_to_database(data, data_type, base_currency, quote_currency):
    conn = sqlite3.connect("gemini_data.db")
    cursor = conn.cursor()

    if data_type == "ticker":
        cursor.execute("""
        INSERT INTO Ticker (base_currency, quote_currency, bid, ask, last)
        VALUES (?, ?, ?, ?, ?);
        """, (base_currency, quote_currency, data['bid'], data['ask'], data['last']))

    elif data_type == "order_book":
        for order_type in ['bids', 'asks']:
            for order in data[order_type]:
                cursor.execute("""
                INSERT INTO OrderBook (base_currency, quote_currency, type, price, amount)
                VALUES (?, ?, ?, ?, ?);
                """, (base_currency, quote_currency, order_type[:-1], order['price'], order['amount']))

    elif data_type == "trade_history":
        for trade in data:
            cursor.execute("""
            INSERT INTO TradeHistory (base_currency, quote_currency, timestamp, price, amount)
            VALUES (?, ?, ?, ?, ?);
            """, (base_currency, quote_currency, trade['timestamp'], trade['price'], trade['amount']))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()

    trading_pair = 'btcusd'

    print("Fetching ticker information...")
    ticker = fetch_ticker('btc', 'usd')
    print("Ticker Information: ", ticker)
    save_to_database(ticker, "ticker", 'btc', 'usd')

    print("\nFetching order book...")
    order_book = fetch_order_book('btc', 'usd')
    print("Order Book: ", order_book)
    save_to_database(order_book, "order_book", 'btc', 'usd')

    print("\nFetching trade history...")
    trade_history = fetch_trade_history('btc', 'usd')
    print("Trade History: ", trade_history)
    save_to_database(trade_history, "trade_history", 'btc', 'usd')
