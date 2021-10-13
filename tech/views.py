from django.shortcuts import render
from . models import Contact , Appli , contactus , pay,InqueryForm,Image,Provisional,about_s,comment
from django.conf import settings
from django.db import IntegrityError
# Create your views here.
from django.core.mail import send_mail
def index(request):
    return render(request,'index.html')
def home(request):
    if request.method=='POST':
        c=comment(request.POST)
        c.comment_name = request.POST.get('reviewname').title()
        c.sid=request.POST.get('reviewgmail')
        c.comment_message=request.POST.get('reviewmessage')
        c.save()
    obj=comment.objects.all()
    return render(request,'home.html',{"object":obj})
def contact(request):
    return render(request,'index.html')
def adddata(request):
        p = Contact()
        p.sname = request.POST.get('sname')
        p.sgmail = request.POST.get('sgmail')
        p.smessage = request.POST.get('smessage')
        p.save()
        return render(request, 'home.html')

def pho(request):
    return render(request,'photo.html',)
def Cont(request):
    return render(request,'contact.html')
def about(request):
    ob = about_s.objects.all()
    return render(request, 'about.html', {'speech_key': ob})

def online(request):
    return render(request,'online.html')

def inh(request):
    return render(request,'photo.html')
def inh1(request):
    return render(request,'home.html')
def inh(request):
    return render(request,'photo.html')
# def inh2(request):
#     return render(request,'home.html')
# def inh3(request):
#     return render(request,'home.html')
# def inh4(request):
#     return render(request,'home.html')
# def inh5(request):
#     return render(request,'home.html')
# def inh6(request):
#     return render(request,'home.html')
def course(request):
    return render(request,'computer course.html')
def application(request):
    return render(request,'index.html')
def provisional(request):
    img = Provisional.objects.all()
    key=request.POST.get('pro')
    return render(request, 'pro.html',{'img':img,"key":key})
def application(request):
    return render(request,'online.html')
def application_datails(request):
        A = Appli(request.POST,request.FILES)
        A.sid = request.POST.get('sid')
        A.name = request.POST.get('name')
        A.Father = request.POST.get('Father')
        A.Mother = request.POST.get('Mother')
        A.Gender = request.POST.get('Gender')
        A.DateBirth = request.POST.get('DateBirth')
        A.Category = request.POST.get('Category')
        A.Occupation = request.POST.get('Occupation')
        A.Disability = request.POST.get('Disability')
        A.AddressLine1 = request.POST.get('AddressLine1')
        A.AddressLine2 = request.POST.get('AddressLine2')
        A.AddressLine3 = request.POST.get('AddressLine3')
        A.City = request.POST.get('City')
        A.State = request.POST.get('State')
        A.District = request.POST.get('District')
        A.Pin = request.POST.get('Pin')
        A.Highest_Educational_Qualification = request.POST.get('Highest_Educational_Qualification')
        A.YearOfPassing = request.POST.get('YearOfPassing')
        A.Aadhar_Card_Number = request.POST.get('Aadhar_Card_Number')
        # A.Upload_Photo = request.POST.get('Upload_Photo')
        # A.Upload_Signature = request.POST.get('Upload_Signature')
        # A.Left_Hand_Thumb_Impression = request.POST.get('Left_Hand_Thumb_Impression')
        docfile = request.FILES['Upload_Photo']
        A.Upload_Photo = docfile
        docfile_sign = request.FILES['Upload_Signature']
        A.Upload_Signature = docfile_sign
        docfile_thumb = request.FILES['Left_Hand_Thumb_Impression']
        A.Left_Hand_Thumb_Impression= docfile_thumb
        A.save()
        return render(request, 'form.html',{"formdata":A})
# def adata(request):
#         A = Appli()
def contactusform(request):
    C=contactus()
    email_from = settings.EMAIL_HOST_USER
    C.name = request.POST.get('name')
    C.Gmail = request.POST.get('Gmail')
    C.number = request.POST.get('number')
    C.message = request.POST.get('message')
    recipient_list = [C.Gmail, ]
    send_mail(C.name, C.message, email_from, recipient_list)
    C.save()
    return render(request, 'home.html',)
def payment(request):
    return render(request,'payment.html')


def order(request):
    p=pay(request.POST)
    p.sid=request.POST.get('sid')
    p.name = request.POST.get('name')
    p.Fathername = request.POST.get('Fathername')
    p.number = request.POST.get('number')
    p.course = request.POST.get('course')
    p.gmail = request.POST.get('gmail')
    p.address = request.POST.get('address')
    p.city = request.POST.get('city')
    p.state = request.POST.get('state')
    p.save()
    return render(request, 'home.html')
def computer(request):
    return render(request,'computer course.html')
def adca(request):
    return render(request,'ADCA.html')
def dca(request):
    return render(request,'dca.html')
def doap(request):
    return render(request,'doap.html')
def adcp(request):
    return render(request,'ADCP.html')
def dtp(request):
    return render(request,'DTP.html')
def dipwd(request):
    return render(request,'DIPWD.html')
def ccca(request):
    return render(request,'CCCA.html')
def rgcit(request):
    return render(request,'RG-CIT.html')
def pgdca(request):
    return render(request,'PGDCA.html')
def dcad(request):
    return render(request,'dcad.html')
def dctt(request):
    return render(request,'dctt.html')
def dpctt(request):
    return render(request,'dpctt.html')
def dcaa(request):
    return render(request,'dcaa.html')
def ccoai(request):
    return render(request,'ccoai.html')
def dmm(request):
    return render(request,'dmm.html')
def CCSUT(request):
    return render(request,'CCSUT.html')
def DIT(request):
    return render(request,'DIT.html')
def PGDIT(request):
    return render(request,'PGDIT.html')
def ADCAWEB(request):
    return render(request,'ADCAWEB.html')
def DMA(request):
    return render(request,'DMA.html')
def DCH(request):
    return render(request,'DCH.html')
def ADCHN(request):
    return render(request,'ADCHN.html')
def NTT(request):
    return render(request,'NTT.html')
def AECPA(request):
    return render(request,'AECPA.html')
def IKO(request):
    return render(request,'IKO.html')
def CTP(request):
    return render(request,'CTP.html')

def mobile(request):
    return render(request,'mobile.html')

def fine(request):
    return render(request,'fine.html')
def bc(request):
    return render(request,'bc.html')
def inh6(request):
    return render(request,'home.html')

def cut(request):
    return render(request,'cut.html')
def draw(request):
    return render(request,'draw.html')
def dance(request):
    return render(request,'dance.html')
def cad(request):
    return render(request,'cad.html')

def inquery(request):
    return render(request,'inquery.html')

def inqueryform(request):
    f = InqueryForm(request)
    f.sid = request.POST.get('sid')
    f.name = request.POST.get('name')
    f.number = request.POST.get('number')
    f.course = request.POST.get('course')
    f.gmail = request.POST.get('gmail')
    f.message = request.POST.get('message')
    f.save()
    return render(request, 'home.html')
def af(request):
    return render(request,'AF.html')

def appform(request):
    f = Appli.objects.all()
    key=request.POST.get('key')
    return render(request , 'form.html' , {"studentdata":f,"key":key})

# def addteacher(request):
#     obj=tea.objects.all()
#     return render(request,'addteacher.html',{'prdt':obj})
def video_file(request):
    return render(request,'video.html')

def student_review(request):
    ob=comment.objects.all()
    for i in ob:
        print(ob.speech)
    return render(request,'about.html',{'speech_key':ob})
