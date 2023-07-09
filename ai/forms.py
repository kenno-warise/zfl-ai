from django import forms

from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill


class ImageUploadForm(forms.Form):
    file = forms.ImageField(label='画像ファイル')

    """ Djangoの画像を加工してくれる機能
    file = ProcessedImageField(spec_id='画像ファイル',
                            processors=[ResizeToFill(50, 50)],
                            format='JPEG',
                            options={'quality':60})
    """
