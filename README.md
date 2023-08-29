# Gemini Public API  
This is a **Python** script that demonstrates how to fetch ticker price, order book, and trade history information for a particular trading pair (e.g., BTCUSD), then stores the fetched data into an **SQLite database** convenient for a proof-of-concept or for local data storage and for further **Analysis Use**.  

### Ticker Table (Limit 5 Row)  
| id | base\_currency | quote\_currency | bid | ask | last | f\_upload\_timestamp |  
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |  
| 1 | btc | usd | 26123.81 | 26126.16 | 26126.17 | 2023-08-28 23:28:11 |  
| 2 | btc | usd | 26116.32 | 26118.61 | 26118.67 | 2023-08-28 23:29:55 | 

### OrderBook Table (Limit 5 Row)  
| id | base\_currency | quote\_currency | type | price | amount | f\_upload\_timestamp |  
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |  
| 1 | btc | usd | bid | 26123.81 | 0.04977 | 2023-08-28 23:28:11 |  
| 2 | btc | usd | bid | 26122.41 | 0.05 | 2023-08-28 23:28:11 |  
| 3 | btc | usd | bid | 26122.4 | 0.3905 | 2023-08-28 23:28:11 |  
| 4 | btc | usd | bid | 26122.01 | 0.05735 | 2023-08-28 23:28:11 |  
| 5 | btc | usd | bid | 26118.88 | 0.25 | 2023-08-28 23:28:11 |  

### TradeHistory Table (Limit 5 Row)  
| id | base\_currency | quote\_currency | timestamp | tid | price | amount | exchange | type | f\_upload\_timestamp |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | btc | usd | 1693270637 | 193568245851 | 26132.49 | 0.00182802 | gemini | buy | 2023-08-29 00:58:34 |
| 2 | btc | usd | 1693270559 | 193568136893 | 26133.75 | 0.0195 | gemini | sell | 2023-08-29 00:58:34 |
| 3 | btc | usd | 1693270477 | 193568050462 | 26138.65 | 0.16829976 | gemini | buy | 2023-08-29 00:58:34 |
| 4 | btc | usd | 1693270477 | 193568050460 | 26138.65 | 0.05732 | gemini | buy | 2023-08-29 00:58:34 |
| 5 | btc | usd | 1693270477 | 193568050458 | 26138.64 | 0.05 | gemini | buy | 2023-08-29 00:58:34 |


  
[Gemini Public API](https://docs.gemini.com/rest-api/#symbols)