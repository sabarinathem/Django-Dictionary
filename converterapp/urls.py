from os import name
from tkinter import mainloop
from django.urls import path
from converterapp import views
urlpatterns=[
    path('',views.startpage,name='startpage'),
    path('index/',views.index,name="index"),
    path('hearbyvoice/',views.HearByVoice,name="hearbyvoice"),
    path('stop/',views.stopvoice,name="stopvoice"),
    path('lang_convert_from_image/',views.lang_convert_from_image,name="lang_convert_from_image"),
    path('image_text_translation/',views.image_text_translation,name="image_text_translation")
]