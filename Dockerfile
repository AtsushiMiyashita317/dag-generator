FROM python:3.11-slim

# 追加：Graphvizと日本語フォントのインストール
RUN apt-get update && \
    apt-get install -y graphviz fonts-noto-cjk && \
    rm -rf /var/lib/apt/lists/*

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリのコピー
COPY . .

# Uvicornでアプリ起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
