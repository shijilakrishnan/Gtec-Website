"""Gtecwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.index,name='index'),
    path('about-us',views.about,name='about-us'),
    path('courses',views.courses,name='courses'),
    path('placement',views.placement,name='placement'),
    path('affiliations',views.affiliations,name='affiliations'),
    path('contact-us',views.contact,name='contact-us'),
    path('accounting',views.accounting,name='accounting'),
    path('software',views.software,name='software'),
    path('multimedia',views.multimedia,name='multimedia'),
    path('cadd',views.cadd,name='cadd'),
    path('msoffice',views.msoffice,name='msoffice'),
    path('digitalmarketing',views.digitalmarketing,name='digitalmarketing'),
    path('hardware',views.hardware,name='hardware'),
    path('software/fullstack',views.fullstack,name='fullstack'),
    path('software/pgdca',views.pgdca,name='pgdca'),
    path('software/mse',views.mse,name='mse'),
    path('software/mdad',views.mdad,name='mdad'),
    path('software/dda',views.dda,name='dda'),
    path('software/ui-ux',views.ui,name='ui/ux'),
    path('software/Geep',views.geep,name='Geep'),
    path('software/Android',views.Android,name='Android'),
    path('software/CCDS',views.CCDS,name='CCDS'),
    path('software/CCDA',views.CCDA,name='CCDA'),
    path('software/Django',views.Django,name='Django'),
    path('software/Figma',views.Figma,name='Figma'),
    path('software/Java SE',views.JavaSE,name='JavaSE'),
    path('software/Java EE',views.JavaEE,name='JavaEE'),
    path('software/Mysql',views.Mysql,name='Mysql'),
    path('software/Python',views.Python,name='Python'),
    path('software/ADDA',views.ADDA,name='ADDA'),
    path('software/DWD',views.DWD,name='DWD'),
    path('software/DDE',views.DDE,name='DDE'),
    path('software/C',views.c,name='C'),
    path('software/CPP',views.cpp,name='CPP'),
    path('caad/adba',views.adba,name='adba'),
    path('caad/adid',views.adid,name='adid'),
    path('caad/dba',views.dba,name='dba'),
    path('caad/did',views.did,name='did'),
    path('caad/AV',views.AV,name='AV'),
    path('caad/AC',views.AC,name='AC'),
    path('caad/Lumion',views.Lumion,name='Lumion'),
    path('caad/Sketchup',views.Sketchup,name='Sketchup'),
    path('caad/Revit',views.Revit,name='Revit'),
    path('caad/A3DS',views.A3DS,name='A3DS'),
    path('hardware/dcss',views.dcss,name='dcss'),
    path('hardware/computer_hardware',views.ch,name='ch'),
    path('hardware/chsi',views.chsi,name='chsi'),
    path('hardware/hdchn',views.hdchn,name='hdchn'),
    path('hardware/cctv',views.cctv,name='cctv'),
    path('software/AO',views.ao,name='AO'),
    path('software/GO',views.go,name='GO'),
    path('software/Dataentry',views.Dataentry,name='Dataentry'),
    # path('software/MSAccess',views.MSAccess,name='MSAccess'),
    path('software/CTTC',views.CTTC,name='CTTC'),
    path('software/CTTP',views.CTTP,name='CTTP'),
    path('software/DCA',views.DCA,name='DCA'),
    path('msoffice/adv',views.adv,name='adv'),
    path('multimedia/mdda',views.mdda,name='mdda'),
    path('multimedia/DA',views.DA,name='DA'),
    path('multimedia/ddi',views.ddi,name='ddi'),
    path('multimedia/dgd',views.dgd,name='dgd'),
    path('multimedia/digitalmrkt',views.digitalmrkt,name='digitalmrkt'),
    path('multimedia/dma',views.dma,name='dma'),
    path('multimedia/dtp',views.dtp,name='dtp'),
    path('multimedia/dve',views.dve,name='dve'),
    path('multimedia/dwa',views.dwa,name='dwa'),
    path('multimedia/gwe',views.gwe,name='gwe'),
    path('multimedia/mdma',views.mdma,name='mdma'),
    path('multimedia/motiongraphics',views.motiongraphics,name='motiongraphics'),
    path('multimedia/PDDM',views.PDDM,name='PDDM'),
    path('accounting/difa',views.difa,name='difa'),
    path('accounting/gccvaat',views.gccvaat,name='gccvaat'),
    path('accounting/pdifas',views.pdifas,name='pdifas'),
    path('accounting/quickbook',views.quickbook,name='quickbook'),
    path('accounting/tallyprime',views.tallyprime,name='tallyprime'),
    path('accounting/sage50',views.sage,name='sage50'),
    path('accounting/gsttally',views.gsttally,name='gsttally'),
    path('accounting/simulation',views.simulation,name='simulation'),
    path('accounting/fico',views.fico,name='fico'),
    path('accounting/mm',views.mm,name='mm'),
    path('accounting/sd',views.sd,name='sd'),
    path('accounting/pp',views.pp,name='pp'),
    path('digitalmarketing/pddm',views.pddm,name='pddm'),
    path('digitalmarketing/cdm',views.cdm,name='cdm'),
    path('digitalmarketing/ddm',views.ddm,name='ddm'),
    path('resume',views.resume,name='resume'),
    path('resume1',views.resume1,name='resume1'),
    path('resume2',views.resume2,name='resume2'),
    path('resume3',views.resume3,name='resume3'),
    path('enquiry',views.enquiry,name="enquiry"),
    # path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    # path('', views.homepage, name='index'),
  
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
