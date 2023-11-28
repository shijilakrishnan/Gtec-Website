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
    path('hardware',views.hardware,name='hardware'),
    path('software/fullstack',views.fullstack,name='fullstack'),
    path('software/pgdca',views.pgdca,name='pgdca'),
    path('software/mse',views.mse,name='mse'),
    path('software/mdad',views.mdad,name='mdad'),
    path('software/dda',views.dda,name='dda'),
    path('software/ui/ux',views.ui,name='ui/ux'),
    path('software/geep',views.geep,name='geep'),
    path('caad/adba',views.adba,name='adba'),
    path('caad/adid',views.adid,name='adid'),
    path('caad/dba',views.dba,name='dba'),
    path('caad/did',views.did,name='did'),
    path('hardware/dcss',views.dcss,name='dcss'),
    path('msoffice/ao',views.ao,name='ao'),
    path('msoffice/go',views.go,name='go'),
    path('msoffice/adv',views.adv,name='adv'),
    path('multimedia/mdda',views.mdda,name='mdda'),
    path('multimedia/da',views.da,name='da'),
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
    path('accounting/difa',views.difa,name='difa'),
    path('accounting/gccvaat',views.gccvaat,name='gccvaat'),
    path('accounting/pdifas',views.pdifas,name='pdifas'),
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
