不動産データ スクレイピングツール（SUUMO）

Python（Requests / BeautifulSoup / pandas）を使用して、
SUUMO の賃貸物件一覧ページから以下の情報を取得するツールです。

物件名

住所

家賃

間取り

■ 使用技術

Python 3.x

requests

BeautifulSoup4

pandas

■ ファイル構成
scraping-suumo/
│
├─ scrape_suumo.py # スクレイピング本体
├─ sample_output.csv # 出力サンプル
└─ README.md

■ 使い方
python scrape_suumo.py

実行すると、sample_output.csv が生成されます。

■ 出力される CSV 例（最初の数行）
物件名 住所 家賃 間取り
■ 目的

スクレイピング学習用

不動産データの収集自動化

ポートフォリオ（案件応募時の実績提示）
