import streamlit as st
import pandas as pd

st.title("先生専用時間割アプリ - テスト版")

st.write("これはテストアプリです。デプロイ確認用。")

# サンプルのデータを表示
data = {
    "日付": ["10月2日", "10月7日"],
    "先生": ["浅田先生", "石倉先生"],
    "生徒": ["林優真", "坂口凛"]
}
df = pd.DataFrame(data)
st.table(df)
