import yfinance as yf
import matplotlib.pyplot as plt

#stock_symbolに代入
stock_symbol = input('株のティッカーシンボルを入力してください（例：AAPL）')

#yf.Tickerでティッカーシンボルに関連する情報を取得
stock = yf.Ticker(stock_symbol)

#期間の選択
#選択肢の表示
print('期間を選んでください')
print('１:１ヶ月')
print('２：３ヶ月')
print('３：１年')
print('４：全期間')

select = int(input('番号を入力してください'))

#選択肢の処理
if select == 1:
  period = '1mo'
elif select == 2:
  period = '3mo'
elif select == 3:
  period = '1y'
elif select == 4:
  period = 'max'
else:
  print('有効な選択肢を入力してください')

#取得するデータの期間設定
stock_data = stock.history(period = period)

#移動平均線を追加
stock_data['5-day MA'] = stock_data['Close'].rolling(window=5).mean()
stock_data['20-day MA'] = stock_data['Close'].rolling(window=20).mean()

#stock_data.indexに日付が入っている感じ、closeは終値
plt.plot(stock_data.index, stock_data['Close'], label='Close Price', color='blue')
plt.plot(stock_data.index, stock_data['5-day MA'], label='5-day MA', color='green')
plt.plot(stock_data.index, stock_data['20-day MA'], label='20-day MA', color='red')
#終値は青、5日と20日の移動平均線がそれぞれ緑と赤

plt.title(f'{stock_symbol} Stock Price with moving averages({period})')
plt.xlabel('Date')
plt.ylabel('Price (USD)')

#グラフにラインの名前を表示
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()