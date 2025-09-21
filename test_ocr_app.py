import streamlit as st
import pandas as pd
import pytesseract
from PIL import Image
import io
import os

st.title("📷 スクショアップロード → OCR 自動更新")

# ファイルアップロード
uploaded_file = st.file_uploader("スクショをアップロードしてください", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 画像読み込み
    image = Image.open(uploaded_file)

    # OCR実行
    text = pytesseract.image_to_string(image, lang="jpn")

    st.subheader("📑 OCR結果")
    st.text(text)

    # デモ用：OCR結果を行ごとに処理
    rows = [line.split() for line in text.splitlines() if line.strip()]

    # CSVに保存（シンプルに teacher, student 形式）
    df = pd.DataFrame(rows, columns=["先生名", "生徒名"]) if rows else pd.DataFrame(columns=["先生名", "生徒名"])

    csv_path = "students.csv"
    if os.path.exists(csv_path):
        old_df = pd.read_csv(csv_path)
        new_df = pd.concat([old_df, df], ignore_index=True)
    else:
        new_df = df

    new_df.to_csv(csv_path, index=False, encoding="utf-8-sig")

    st.success("✅ students.csv を更新しました！")
    st.dataframe(new_df)
