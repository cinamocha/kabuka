# 株価情報取得アプリ(kabuka)  
株価情報を取得するPythonアプリ。指定した銘柄の最新の株価を取得し表示します。  

## 概要  
- **ジャンル**:株価情報取得アプリ
- **目的**:指定した銘柄の最新の株価情報を取得して表示する
- **機能**:
  - ユーザーが指定した銘柄の株価を表示
  - リアルタイムで株価情報を表示
  - 株価情報をグラフで表示

## 追加機能  
5日移動平均線と20日移動平均線も表示されるようにしました。トレンドが一目でわかります。  
  
## 使用技術  
- **プログラミング言語**:Python
- **ライブラリ**:yfinance matplotlib

## 使い方  
1. **Pythonをインストール**
   [公式サイト](https://www.python.org/)からインストールしてください。
   
2. **クローンorダウンロード**
```
git clone https://github.com/cinamocha/kabuka
cd kabuka
```
  
3. **ライブラリのインストール**
```
pip install yfinance
pip install matplotlib
```

4. 実行
```
python kabuka.py
```
