from django.shortcuts import render
from .forms import SimpleUploadForm, ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .cv_functions import cv_detect_face

# Create your views here.
def first_view(request):
    return render(request, 'opencv_webapp/first_view.html',{})


# def simple_upload(request):
#
#
#     form = SimpleUploadForm()
#     context = {'form':form}
#     return render (request, 'opencv_webapp/simple_upload.html', context)

# temp comments
def simple_upload(request):
    if request.method == 'POST':
        # print(request.POST) : <QueryDict: {'csrfmiddlewaretoken': [‘~~~’], 'title': ['upload_1']}>
        # print(request.FILES) : <MultiValueDict: {'image': [<InMemoryUploadedFile: ses.jpg (image/jpeg)>]}>
        # 비어있는 Form에 사용자가 업로드한 데이터를 넣고 검증합니다.
        form = SimpleUploadForm(request.POST, request.FILES)

        if form.is_valid():
            myfile = request.FILES['image'] # 'ses.jpg'
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile) # 경로명을 포함한 파일명 & 파일 객체

            # 업로드된 이미지 파일의 URL을 얻어내 Template에게 전달
            uploaded_file_url = fs.url(filename) # '/media/ses.jpg'

            context = {'form': form, 'uploaded_file_url': uploaded_file_url} # filled form
            return render(request, 'opencv_webapp/simple_upload.html', context)

    else: # request.method == 'GET' (DjangoBasic 실습과 유사한 방식입니다.)
        form = SimpleUploadForm()
        context = {'form': form} # empty form
        return render(request, 'opencv_webapp/simple_upload.html', context)


def detect_face(request):

    if request.method == 'POST' :
        # 비어있는 Form에 사용자가 업로드한 데이터를 넣고 검증합니다.
        form = ImageUploadForm(request.POST, request.FILES) # filled form

        if form.is_valid():
            # Form에 채워진 데이터를 DB에 실제로 저장하기 전에 변경하거나 추가로 다른 데이터를 추가할 수 있음
            post = form.save(commit=False)


            # 주석 라인에서 임시저장하고 추가 작업을 하는 경우에 윗줄처럼 save처리했음
            # ex) post.description = post.description.lower()

            post.save() # DB에 실제로 Form 객체('form')에 채워져 있는 데이터를 저장
            # post는 save() 후 DB에 저장된 ImageUploadModel 클래스 객체 자체를 갖고 있게 됨 (record 1건에 해당)

            imageURL = settings.MEDIA_URL + form.instance.document.name
            # imageURL = '/media/images/2020/02/21/test_image.jpg'
            # document : ImageUploadModel Class에 선언되어 있는 “document”에 해당
            # print(form.instance, form.instance.document.name, form.instance.document.url)

            cv_detect_face(settings.MEDIA_ROOT_URL + imageURL) # 추후 구현 예정
            # 얼굴인식


            # 모델 적용할때
            # keras_models.py -> keras_predict_malig() # 모델 미리 저장해두고
            # keras_predicted_class = keras_predict_malig(???)

            return render(request, 'opencv_webapp/detect_face.html', {'form':form, 'post':post})

    else:
         form = ImageUploadForm() # empty form
         return render(request, 'opencv_webapp/detect_face.html', {'form':form})
