import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Python講習会_画像アップロード＆表示", layout="centered")

st.title("🖼️ Python講習会＿画像uploader")
st.write("画像をアップロードすると、すぐに下に表示されます。")

uploaded_file = st.file_uploader("画像をドラッグ＆ドロップ、または選択してください", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.success("画像がアップロードされました！")
    image = Image.open(uploaded_file)
    st.image(image, caption="アップロードされた画像", use_column_width=True)
