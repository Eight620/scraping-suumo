# 不動産データ スクレイピングツール（SUUMO）

Python（Requests / BeautifulSoup / pandas）を使用して  
SUUMO の賃貸物件一覧ページから物件情報を自動で取得するツールです。

---

## 📌 概要

このツールは、指定した SUUMO 賃貸検索ページから以下の情報を取得して  
CSV に保存します。

- 物件名  
- 住所  
- 家賃  
- 間取り  

スクレイピング学習やポートフォリオ、  
クライアント向けのデータ収集ツールとして利用できます。

---

## 🛠 使用技術

- Python 3.x  
- requests  
- BeautifulSoup4  
- pandas  

---

## 📂 ファイル構成

scraping-suumo/
│
├─ scrape_suumo.py # スクレイピング本体
├─ sample_output.csv # 出力サンプル
└─ README.md

---

## 🚀 使い方

### 1. ライブラリをインストール

pip install requests beautifulsoup4 pandas
2. 実行
bash
コードをコピーする
python scrape_suumo.py
3. 出力
同じディレクトリに sample_output.csv が生成されます。

📄 出力されるCSV例（最初の数行）
物件名	住所	家賃	間取り
○○マンション	東京都新宿区○○	12.3万円	1K
△△アパート	東京都新宿区△△	8.7万円	1R

📝 注意事項
当ツールは個人学習・ポートフォリオ用です

公開されているページのみを対象とし、利用規約に反しない範囲で使用します

大量アクセスや高頻度の取得は避けてください

🎯 今後の拡張（想定）
ページネーション対応

物件詳細ページの追加情報取得

複数エリアの一括取得

データの自動整形（pandas）

Google スプレッドシートへの自動出力

👤 制作者
名前：Eight

学習歴：HTML/CSS, Java, Python, C

強み：スクレイピング／データ加工（pandas）／自動化ツールの作成

