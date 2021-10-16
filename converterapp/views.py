from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from googletrans import Translator
import googletrans
from gtts import gTTS
from playsound import playsound
from converterapp import vlc
# from pygame import mixer
import time
# from pydub import AudioSegment
import pytesseract as pyt
from PIL import Image
from converterapp.models import Audio
from django.core.files import File
# import pyttsx3

# engine=pyttsx3.init()
# engine.runAndWait()


# from converterapp.models import Image
# Create your views here.
def startpage(request):
    return render(request,'converterapp/startpage.html')

def index(request):
    # try:



    import os, shutil
    folder = 'media/audio'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    # return HttpResponse('delete the audio files')

    if request.method=="POST":
        a=Audio()
        Audio.objects.all().delete()
        word=request.POST["word"]
        language=request.POST["lang"]
        translator=Translator()
        translate=translator.translate(word,dest=language)
        trans_text=translate.text
        
        ts=gTTS(trans_text,lang=language,slow=False)
        ts.save("voice.mp3")
        file=File(open('voice.mp3','rb'))
       
        a.audio=file
        a.save()

        audio=Audio.objects.raw('select * from converterapp_audio where id=(SELECT MAX(id) FROM converterapp_audio)')
         
        context={'convert':trans_text,'lang':language,'item':audio}   

        
        return render(request,'converterapp/convert.html',context)
    # except:
    #     return HttpResponse('No internet, Please try to connect Internet')
    
    return render(request,'converterapp/index.html')
# def HearByVoice(request):
  
#     if request.method=="POST":
#         word=request.POST["word"]
#         language=request.POST["lang"]
#         print(language)
#         ts=gTTS(word,lang=language,slow=False)
#         ts.save("voice.mp3")
#         # global p
#         # p = vlc.MediaPlayer("voice.mp3")
#         # p.play()
       
#         # AudioSegment.from_mp3("voice.mp3").export('voice.ogg', format='ogg')
#         # mixer.init() #Initialzing pyamge mixer

#         # mixer.music.load('voice.ogg') #Loading Music File

#         # mixer.music.play() #Playing Music with Pygame

            


#             # mixer.music.stop()
#         return render(request,'converterapp/convert.html',{'convert':word,'lang':language})
  
# def stopvoice(request):
#     try:
        
#         if request.method=="POST":
#             convert=request.POST["word"]
#             language=request.POST["lang"]
#             # return HttpResponse(language)
#             return render(request,'converterapp/convert.html',{'convert':convert,'lang':language})
#     except:
#         return HttpResponse('No internet, Please try to connect Internet')
def lang_convert_from_image(request):
    
   
    return render(request,'converterapp/convert_from_image.html')

def image_text_translation(request):
    
    import PIL.Image
    if request.method=="POST":
            #Image database
            # img=Image()
            
            
            # image=request.["image"]
        if len(request.FILES)!=0:
            image=request.FILES["image"]
                    
            # img.pimage=image
            # img.save()
        a=Audio()    
        src=request.POST["pytname"]
        dest=request.POST["googletransname"]
                
        
        img = PIL.Image.open(image)
                
        text=pyt.image_to_string(img,lang=src)
        text=text.replace("\n",' ')

        translator=Translator()
        translate=translator.translate(text,dest=dest)
        trans_text=translate.text
        ts=gTTS(trans_text,lang=dest,slow=False)
        ts.save("voice.mp3")
        file=File(open('voice.mp3','rb'))
       
        a.audio=file
        a.save()

        audio=Audio.objects.raw('select * from converterapp_audio where id=(SELECT MAX(id) FROM converterapp_audio)')
         
        context={'convert':trans_text,'lang':dest,'item':audio}   

        
        return render(request,'converterapp/convert.html',context)
    # except:
    #      return HttpResponse('No internet, Please try to connect Internet')
   
        
       
    
        
       