import numpy as np  # type: ignore
from django.test import TestCase  # type: ignore
from django.urls import reverse  # type: ignore
from PIL import Image

from ai.cat_cnn import predict


def sample_img():
    img = Image.open("ai/static/ai/cat_1.jpg").resize((50, 50)).convert("RGB")

    img_array = np.asarray(img)
    img_cmp = []
    img_cmp.append(img_array)
    img_cmp = np.array(img_cmp)
    return img_cmp


class PredictTests(TestCase):
    def test_predict(self):
        """
        予測結果を返すcat_cnn.pyのpredict関数のテスト
        """
        img = sample_img()
        result = predict(img)
        self.assertIsInstance(result, str, "戻り値は文字列")


# ビューのテスト
class IndexViewTests(TestCase):
    def test_ai_pageview(self):
        """
        /ai/の表示テスト
        """
        response = self.client.get(reverse("ai:index"))
        self.assertEqual(response.status_code, 200)

    def test_ai_result(self):
        """
        /ai/の結果表示
        """
        with open("ai/static/ai/cat_1.jpg", "rb") as f:
            response = self.client.post(reverse("ai:index"), {"file": f})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "猫")
        self.assertContains(response, "ライオン")
        self.assertContains(response, "チーター")


# Create your tests here.
