FROM python:3.11-slim

# 必要なツールのインストール
RUN apt-get update && apt-get install -y graphviz && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリ作成
WORKDIR /app

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリ本体をコピー
COPY . .

# 起動コマンド
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
