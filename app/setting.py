# --------------------------------------------------------------------------------
# FashionMNIST情報
# --------------------------------------------------------------------------------
# ラベル名(日)
CLASSES_JA = [
    "Tシャツ / トップ", "スボン", "プルオーバー", "ドレス", "コード",
    "サンダル", "ワイシャツ", "スニーカー", "バッグ", "アンクルブーツ",
]

# ラベル名(英)
CLASSES_EN = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

# クラス数
N_CLASS = len(CLASSES_JA)

# 画像サイズ
IMG_SIZE = 28


# --------------------------------------------------------------------------------
# 学習済みモデル情報
# --------------------------------------------------------------------------------
# 学習済みモデルのパラメータ
TRAIN_MODEL_PATH = "../ml/model_param/latest_train_model.pth"


# --------------------------------------------------------------------------------
# アプリ情報
# --------------------------------------------------------------------------------
# アプリ名
APP_TITLE = "画像認識アプリ"

# アプリ説明
APP_DESCRIPTION = "画像の衣服の種類を判定します。"

# コピーライト表示
# NOTE: FashionMNIST使用しているため記載必要
COPYRIGHT_TEXT = """
このアプリは、「Fashion-MNIST」を訓練データとして使っています。\n
Copyright (c) 2017 Zalando SE\n
Released under the MIT license\n
https://github.com/zalandoresearch/fashion-mnist#license
"""

# 画像拡張子
IMG_EXT_LIST = ["png", "jpg", "jpeg"]

# 画像ソースタイプ
IMG_SRC_UPLOAD = "画像アップロード"
IMG_SRC_CAMERA = "カメラ撮影"

# 画像認識結果表示のトップ数
# NOTE: 指定した数だけ順位表示する
RESULT_N_TOP = 5

# 入力画像の表示幅
DISPLAY_IMG_WIDTH = 480 // 2
