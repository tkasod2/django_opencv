from django.contrib import admin

# Register your models here.
from .models import ImageUploadModel

class ImageUploadAdmin(admin.ModelAdmin):

    list_display = ('description', 'document', )
    # list_display 변수명은 고정
    #

admin.site.register(ImageUploadModel, ImageUploadAdmin)
# admin page에 사진 올리는 창 만들기
