from . import views
from django.urls import path
urlpatterns = [
path('',views.home),
path('home',views.home),
path('contact', views.contact),
path('photo',views.pho),
path('aboutus', views.about),
path('index',views.inh),
# path('index',views.inh1),
# path('index',views.inh2),
# path('index',views.inh3),
# path('index',views.inh4),
# path('index',views.inh5),
# path('index',views.inh6),
path('adddata', views.adddata),
path('Contact',views.Cont),
#path('sendmail',views.sendmail),
path('online',views.online),
path('computer',views.course),
path('provisional',views.provisional),
path('application',views.application),
path('application_datails',views.application_datails),
path('contactusform',views.contactusform),
path('payment',views.payment),
path('order',views.order),
path('adca',views.adca),
path('computer',views.computer),
path('dca',views.dca),
path('doap',views.doap),
path('adcp',views.adcp),
path('dtp',views.dtp),
path('dipwd',views.dipwd),
path('ccca',views.ccca),
path('rgcit',views.rgcit),
path('pgdca',views.pgdca),
path('dcad',views.dcad),
path('dctt',views.dctt),
path('dpctt',views.dpctt),
path('dcaa',views.dcaa),
path('ccoai',views.ccoai),
path('dmm',views.dmm),
path('ccsut',views.CCSUT),
path('dit',views.DIT),
path('pgdit',views.PGDIT),
path('adcaweb',views.ADCAWEB),
path('dma',views.DMA),
path('dch',views.DCH),
path('adchn',views.ADCHN),
path('ntt',views.NTT),
path('aecpa',views.AECPA),
path('iko',views.IKO),
path('ctp',views.CTP),
path('mobile',views.mobile),
path('fine',views.fine),
path('bc',views.bc),
path('cut',views.cut),
path('draw',views.draw),
path('dance',views.dance),
path('cad',views.cad),
path('inquery',views.inquery),
path('inqueryform',views.inqueryform),
path('af',views.af),
path('appform',views.appform),
path('video_file',views.video_file),


]