import yfinance as yf
import matplotlib.pyplot as plt

#stock_symbolに代入
stock_symbol = input('株のティッカーシンボルを入力してください（例：AAPL）')

#yf.Tickerでティッカーシンボルに関連する情報を取得
stock = yf.Ticker(stock_symbol)

#取得するデータの期間設定
stock_data = stock.history(period = '1mo')

#stock_data.indexに日付が入っている感じ、closeは終値
plt.plot(stock_data.index, stock_data['Close'])

plt.title(f'{stock_symbol} Stock Price')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()