from django.test import TestCase
from django.urls import reverse
from PIL import Image
import numpy as np

from ai.cat_cnn import predict
from ai.views import IndexView


def sample_img():
    img = Image.open('ai/static/ai/cat_1.jpg').resize((50, 50)).convert('RGB')

    img_array = np.asarray(img)
    X = []
    X.append(img_array)
    X = np.array(X)
    return X


class PredictTests(TestCase):

    def test_predict(self):
        """
        予測結果を返すcat_cnn.pyのpredict関数のテスト
        """
        img = sample_img()
        result = predict(img)
        self.assertIsInstance(result, str, '戻り値は文字列')


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
        with open('ai/static/ai/cat_1.jpg', 'rb') as f:
            response = self.client.post(reverse("ai:index"), {'file':f})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '猫')
        self.assertContains(response, 'ライオン')
        self.assertContains(response, 'チーター')

# Create your tests here.
