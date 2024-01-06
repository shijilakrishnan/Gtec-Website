from django.core.mail import send_mail
from django.shortcuts import render,redirect
from .models import Admission,Placements
from django.contrib import messages
# import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest



# Create your views here.
def index(request):
    images = Placements.objects.all()
    return render(request,'index.html',{'images':images})

def about(request):
    return render(request,'about-us.html')

def courses(request):
    return render(request,'courses.html')

def placement(request):
    return render(request,'placement.html')

def affiliations(request):
    return render(request,'affiliations.html')

def contact(request):
    return render(request,'contact-us.html')

def accounting(request):
    return render(request,'accounting/accounting.html')

def software(request):
    return render(request,'software/software.html')

def multimedia(request):
    return render(request,'multimedia/multimedia.html')

def cadd(request):
    return render(request,'caad/cadd.html')

def msoffice(request):
    return render(request,'msoffice/msoffice.html')

def hardware(request):
    return render(request,'hardware/hardware.html')

def fullstack(request):
    return render(request,'software/fullstack.html')

def pgdca(request):
    return render(request,'software/pgdca.html')

def mse(request):
    return render(request,'software/mse.html')

def mdad(request):
    return render(request,'software/mdad.html')

def dda(request):
    return render(request,'software/dda.html')

def ui(request):
    return render(request,'software/ui-ux.html')

def geep(request):
    return render(request,'software/Geep.html')

def ADDA(request):
    return render(request,'software/ADDA.html')
def DWD(request):
    return render(request,'software/DWD.html')
def DDE(request):
    return render(request,'software/DDE.html')
def adba(request):
    return render(request,'caad/adba.html')

def adid(request):
    return render(request,'caad/adid.html')

def dba(request):
    return render(request,'caad/dba.html')

def did(request):
    return render(request,'caad/did.html')

def AV(request):
    return render(request,'caad/AV.html')

def AC(request):
    return render(request,'caad/AC.html')

def Lumion(request):
    return render(request,'caad/Lumion.html')

def Sketchup(request):
    return render(request,'caad/Sketchup.html')

def Revit(request):
    return render(request,'caad/Revit.html')

def A3DS(request):
    return render(request,'caad/A3DS.html')
def dcss(request):
    return render(request,'hardware/dcss.html')

def ao(request):
    return render(request,'software/AO.html')

def go(request):
    return render(request,'software/GO.html')

def adv(request):
    return render(request,'msoffice/adv.html')

def Dataentry(request):
    return render(request,'software/Dataentry.html')

# def MSAccess(request):
#     return render(request,'software/MSAccess.html')
def CTTC(request):
    return render(request,'software/CTTC.html')
def CTTP(request):
    return render(request,'software/CTTP.html')

def DCA(request):
    return render(request,'software/DCA.html')
def mdda(request):
    return render(request,'multimedia/mdda.html')

def motiongraphics(request):
    return render(request,'multimedia/motiongraphics.html')

def mdma(request):
    return render(request,'multimedia/mdma.html')

def gwe(request):
    return render(request,'multimedia/gwe.html')

def dwa(request):
    return render(request,'multimedia/dwa.html')

def dve(request):
    return render(request,'multimedia/dve.html')

def dtp(request):
    return render(request,'multimedia/dtp.html')

def dma(request):
    return render(request,'multimedia/dma.html')

def digitalmrkt(request):
    return render(request,'multimedia/digitalmrkt.html')

def dgd(request):
    return render(request,'multimedia/dgd.html')

def ddi(request):
    return render(request,'multimedia/ddi.html')

def da(request):
    return render(request,'multimedia/da.html')

def difa(request):
    return render(request,'accounting/difa.html')

def gccvaat(request):
    return render(request,'accounting/gccvaat.html')

def pdifas(request):
    return render(request,'accounting/pdifas.html')

def quickbook(request):
    return render(request,'accounting/quickbook.html')

def tallyprime(request):
    return render(request,'accounting/tallyprime.html')

def sage(request):
    return render(request,'accounting/sage50.html')

def gsttally(request):
    return render(request,'accounting/gsttally.html')

def simulation(request):
    return render(request,'accounting/simulation.html')

def fico(request):
    return render(request,'accounting/fico.html')

def mm(request):
    return render(request,'accounting/mm.html')

def pp(request):
    return render(request,'accounting/pp.html')

def sd(request):
    return render(request,'accounting/sd.html')
def resume(request):
    return render(request,'resume.html')

def resume1(request):
    return render(request,'resume1.html')

def resume2(request):
    return render(request,'resume2.html')

def resume3(request):
    return render(request,'resume3.html')

def digitalmarketing(request):
    return render(request,'digitalmarketing/digitalmarketing.html')

def pddm(request):
    return render(request,'digitalmarketing/pddm.html')

def ddm(request):
    return render(request,'digitalmarketing/ddm.html')

def cdm(request):
    return render(request,'digitalmarketing/cdm.html')

def ch(request):
    return render(request,'hardware/computer_hardware.html')

def cctv(request):
    return render(request,'hardware/cctv.html')

def chsi(request):
    return render(request,'hardware/chsi.html')
def hdchn(request):
    return render(request,'hardware/hdchn.html')

def DA(request):
    return render(request,'multimedia/DA.html')

def PDDM(request):
    return render(request,'multimedia/PDDM.html')

def Android(request):
    return render(request,'software/Android.html')

def CCDS(request):
    return render(request,'software/CCDS.html')

def CCDA(request):
    return render(request,'software/CCDA.html')

def Django(request):
    return render(request,'software/Django.html')

def Figma(request):
    return render(request,'software/Figma.html')

def JavaSE(request):
    return render(request,'software/JavaSE.html')

def JavaEE(request):
    return render(request,'software/JavaEE.html')
def Mysql(request):
    return render(request,'software/Mysql.html')

def Python(request):
    return render(request,'software/Python.html')

def c(request):
    return render(request,'software/C.html')

def cpp(request):
    return render(request,'software/CPP.html')
def enquiry(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        dob = request.POST['dob']
        address = request.POST['address']
        place = request.POST['place']
        course = request.POST['course']
        qualification = request.POST['qualification']

        # Check if the email already exists in the database
        if Admission.objects.filter(email=email).exists():
            messages.warning(request, 'Email is Already Exist')
            return render(request, 'enquiry.html')
        else:
            # Create and save the user in the database
            user = Admission.objects.create(
                fname=fname, lname=lname, phone=phone, email=email, dob=dob, address=address, place=place,
                course=course, qualification=qualification
            )

            # Send email to snehae32@gmail.com with user details
            send_mail(
                'New User Enquiry',
                f'Name: {fname} {lname}\nPhone: {phone}\nEmail: {email}\nDOB: {dob}\nAddress: {address}\n'
                f'Place: {place}\nCourse: {course}\nQualification: {qualification}',
                'gtecprogramming@gmail.com',
                ['gtecprogramming@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, "Submitted Successfully")
            return render(request, 'enquiry.html')

    return render(request, 'enquiry.html')
        # send_mail('user details','name:{name}','from@gmail.com',['gtecprogramming@gmail.com'])
        
#         currency = 'INR'
#         amount = 30000  # Rs. 300
    
        
#         razorpay_order = razorpay_client.order.create(dict(amount=amount,
#                                                         currency=currency,
#                                                         payment_capture='0'))
    
        
#         razorpay_order_id = razorpay_order['id']
#         callback_url = 'paymenthandler/'
    
        
#         context = {}
#         context['razorpay_order_id'] = razorpay_order_id
#         context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
#         context['razorpay_amount'] = amount
#         context['currency'] = currency
#         context['callback_url'] = callback_url
    
#         return render(request,'enquiry.html')
#     return render(request,'enquiry.html')



# razorpay_client = razorpay.Client(
#     auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 

# @csrf_exempt
# def paymenthandler(request):
 
#     # only accept POST request.
#     if request.method == "POST":
#         try:
           
#             # get the required parameters from post request.
#             payment_id = request.POST.get('razorpay_payment_id', '')
#             razorpay_order_id = request.POST.get('razorpay_order_id', '')
#             signature = request.POST.get('razorpay_signature', '')
#             params_dict = {
#                 'razorpay_order_id': razorpay_order_id,
#                 'razorpay_payment_id': payment_id,
#                 'razorpay_signature': signature
#             }
 
#             # verify the payment signature.
#             result = razorpay_client.utility.verify_payment_signature(
#                 params_dict)
#             if result is not None:
#                 amount = 30000  # Rs. 200
#                 try:
 
#                     # capture the payemt
#                     razorpay_client.payment.capture(payment_id, amount)
 
#                     # render success page on successful caputre of payment
#                     return render(request, 'paymentsuccess.html')
#                 except:
 
#                     # if there is an error while capturing payment.
#                     return render(request, 'paymentfail.html')
#             else:
 
#                 # if signature verification fails.
#                 return render(request, 'paymentfail.html')
#         except:
 
#             # if we don't find the required parameters in POST data
#             return HttpResponseBadRequest()
#     else:
#        # if other than POST request is made.
#         return HttpResponseBadRequest()

