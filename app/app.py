import streamlit as st
from PIL import Image
from streamlit.runtime.uploaded_file_manager import UploadedFile

from src.model import Model
from src.plot import draw_result_pie_diagram

from setting import APP_TITLE, APP_DESCRIPTION, COPYRIGHT_TEXT
from setting import IMG_EXT_LIST, IMG_SRC_UPLOAD, IMG_SRC_CAMERA
from setting import RESULT_N_TOP, DISPLAY_IMG_WIDTH


def process_sidebar():
    """サイドバーの処理"""
    st.sidebar.title(APP_TITLE)
    st.sidebar.write(APP_DESCRIPTION)
    st.sidebar.write("")

    img_src_type = st.sidebar.radio("画像のソースを選択してください", (IMG_SRC_UPLOAD, IMG_SRC_CAMERA))

    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.caption(COPYRIGHT_TEXT)

    return img_src_type


def get_source_image(img_src_type: str) -> UploadedFile | None:
    """入力画像を取得"""
    if img_src_type == IMG_SRC_UPLOAD:
        img_upload_file = st.sidebar.file_uploader("画像を選択してください", type=IMG_EXT_LIST)
    elif img_src_type == IMG_SRC_CAMERA:
        img_upload_file = st.camera_input("カメラで撮影")
    else:
        img_upload_file = None
    return img_upload_file


def process_main(img_upload_file: UploadedFile) -> None:
    """入力画像を予測し、予測結果を表示する処理"""
    img = Image.open(img_upload_file)
    st.image(img, caption="対象の画像", width=DISPLAY_IMG_WIDTH)
    st.write("")

    # 予測
    results = model.predict(img)

    # 結果の表示
    n_top = RESULT_N_TOP
    st.subheader("判定結果")
    for result in results[:n_top]:
        st.write(f"{round(result.prob*100, 2)}% の確率で 「{result.classes_ja}」 です。")

    # 円グラフの表示
    fig = draw_result_pie_diagram(results, n_top)
    st.pyplot(fig)


if __name__ == "__main__":

    model = Model()

    img_source = process_sidebar()
    img_upload_file = get_source_image(img_source)

    if img_upload_file is not None:
        with st.spinner("推定中..."):
            process_main(img_upload_file)
