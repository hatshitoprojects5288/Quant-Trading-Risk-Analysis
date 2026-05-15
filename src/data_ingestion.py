import requests
import json
import logging

# Data Architecture: OHLCV Crypto Data Ingestion Pipeline

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def fetch_market_data(symbol="BTCUSDT", interval="1d", limit=100):
    """
    Ingests raw OHLCV (Open, High, Low, Close, Volume) data from public exchange APIs.
    Used to feed historical data into the backtesting engine.
    """
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    
    logging.info(f"Establishing connection to data provider for {symbol}...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        parsed_data = []
        for candle in data:
            parsed_data.append({
                "timestamp": candle[0],
                "open": float(candle[1]),
                "high": float(candle[2]),
                "low": float(candle[3]),
                "close": float(candle[4]),
                "volume": float(candle[5])
            })
            
        logging.info(f"Successfully ingested {len(parsed_data)} data points.")
        return parsed_data
        
    except requests.exceptions.RequestException as e:
        logging.error(f"Data ingestion failed: {e}")
        return None

if __name__ == "__main__":
    market_data = fetch_market_data()
    # In a production environment, this data is piped to a SQL database or Pandas DataFrame
