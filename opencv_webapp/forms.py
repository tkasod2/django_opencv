from django import forms
from .models import ImageUploadModel

# 기존방식
# class PostForm(forms.ModelForm):
#         class Meta:
#             mdoel = Model 클래스이름(@models.py)
#             fields = ('Moedel 클래스의 변수명 1', 'Model클래스의 변수명2')


class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    # ImageField Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
    # file = forms.FileField()
    image = forms.ImageField()

class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document')
