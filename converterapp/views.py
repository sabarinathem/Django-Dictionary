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
# import pyttsx3

# engine=pyttsx3.init()
# engine.runAndWait()


# from converterapp.models import Image
# Create your views here.
def startpage(request):
    return render(request,'converterapp/startpage.html')

def index(request):
    try:
        if request.method=="POST":
            word=request.POST["word"]
            language=request.POST["lang"]
            translator=Translator()
            translate=translator.translate(word,dest=language)
            trans_text=translate.text
            context={'convert':trans_text,'lang':language}
        
            return render(request,'converterapp/convert.html',context)
    except:
        return HttpResponse('No internet, Please try to connect Internet')
    return render(request,'converterapp/index.html')
def HearByVoice(request):
  
    if request.method=="POST":
        word=request.POST["word"]
        language=request.POST["lang"]
        print(language)
        ts=gTTS(word,lang=language,slow=False)
        ts.save("voice.mp3")
        global p
        p = vlc.MediaPlayer("voice.mp3")
        p.play()
       
        # AudioSegment.from_mp3("voice.mp3").export('voice.ogg', format='ogg')
        # mixer.init() #Initialzing pyamge mixer

        # mixer.music.load('voice.ogg') #Loading Music File

        # mixer.music.play() #Playing Music with Pygame

            


            # mixer.music.stop()
        return render(request,'converterapp/convert.html',{'convert':word,'lang':language})
  
def stopvoice(request):
    try:
        p.stop()
        if request.method=="POST":
            convert=request.POST["word"]
            language=request.POST["lang"]
            # return HttpResponse(language)
            return render(request,'converterapp/convert.html',{'convert':convert,'lang':language})
    except:
        return HttpResponse('No internet, Please try to connect Internet')
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
            
        src=request.POST["pytname"]
        dest=request.POST["googletransname"]
                
        
        img = PIL.Image.open(image)
                
        text=pyt.image_to_string(img,lang=src)
        text=text.replace("\n",' ')

        translator=Translator()
        translate=translator.translate(text,dest=dest)
        trans_text=translate.text
        context={'convert':trans_text,'lang':dest}
        return render(request,'converterapp/convert.html',context)
    # except:
    #      return HttpResponse('No internet, Please try to connect Internet')
   
        
       
    
        
       