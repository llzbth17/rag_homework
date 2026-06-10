"""Готовит data/raw/datasets.json из ag_news CSV."""
import csv
import json
import urllib.request
from pathlib import Path

RAW = Path("data/raw")
RAW.mkdir(parents=True, exist_ok=True)
CSV_PATH = RAW / "ag_news_train.csv"
OUTPUT = RAW / "datasets.json"

CSV_URL = "https://raw.githubusercontent.com/mhjabreel/CharCnn_Keras/master/data/ag_news_csv/train.csv"
MAX_RECORDS = 1200


def download():
    if CSV_PATH.exists():
        print(f"CSV уже скачан: {CSV_PATH}")
        return
    print(f"Скачиваю CSV...")
    urllib.request.urlretrieve(CSV_URL, CSV_PATH)
    print(f"Сохранено: {CSV_PATH}")


def main():
    download()
    docs = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i >= MAX_RECORDS:
                break
            if len(row) < 3:
                continue
            label, title, description = row[0], row[1], row[2]
            text = f"{title}. {description}".strip()
            if len(text) < 50:
                continue
            docs.append({
                "doc_id": f"agnews_{i:05d}",
                "title": title[:80],
                "text": text,
                "source": f"ag_news (class={label})",
            })

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(docs, f, ensure_ascii=False, indent=2)
    print(f"Сохранено {len(docs)} записей в {OUTPUT}")


if __name__ == "__main__":
    main()
