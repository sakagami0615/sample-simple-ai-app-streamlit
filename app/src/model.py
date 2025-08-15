import torch
from torch import nn
from torchvision import transforms
from PIL import Image

from dataclasses import dataclass
from common.network import Net

from setting import IMG_SIZE, TRAIN_MODEL_PATH, CLASSES_JA, CLASSES_EN


@dataclass
class Result:
    classes_ja: str
    classes_en: str
    prob: float


class Model:

    def __init__(self):
        self._net = self.load_train_model()

    @staticmethod
    def load_train_model(train_model_path: str = TRAIN_MODEL_PATH) -> Net:
        """学習済みモデルを準備

        Args:
            train_model_path (str, optional): パラメータ保存ファイルパス (Defaults to TRAIN_MODEL_PATH)

        Returns:
            Net: 学習済みモデル
        """
        net = Net()
        net.load_state_dict(torch.load(
            train_model_path, map_location=torch.device("cpu")
        ))
        return net

    def predict(self, img: Image, img_size: int = IMG_SIZE) -> list[Result]:
        """学習済みモデルを使用して予測を実施

        Args:
            img (Image): 入力画像
            img_size (int, optional): 入力画像サイズ (Defaults to IMG_SIZE)

        Returns:
            list[tuple[int, int, float]]: 予測結果 (日本語ラベル、英語ラベル、予測確率)
        """
        img = img.convert("L")                      # グレースケール化
        img = img.resize((IMG_SIZE, IMG_SIZE))      # リサイズ

        # 入力データ用意
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.0), (1.0)),
        ])
        img = transform(img)
        x = img.reshape(1, 1, img_size, img_size)

        # 予測
        self._net.eval()
        y = self._net(x)

        # 各ラベルの予測確率が高い順にソート
        y_prob = nn.functional.softmax(torch.squeeze(y))
        sorted_prob, sorted_indices = torch.sort(y_prob, descending=True)

        return [Result(CLASSES_JA[idx], CLASSES_EN[idx], prob.item()) for (idx, prob) in zip(sorted_indices, sorted_prob)]
