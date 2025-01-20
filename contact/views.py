from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

def vm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Email content
        subject = f"New Massage from VM site from {name}"
        email_message = (
            f"hey Mr Bhavik Gajjar You've Got A Mail From Vishwakarma-Mech-Fab Website From {name} \n"
            "-----------------------------------------\n\n"
            "Details of the sender :\n\n"
            "-----------------------------------------\n"
            f"--> Name : {name}\n"
            f"--> Phone Number : {phone}\n"
            f"--> Email ID : {email}\n"
            f"--> Message : {message}\n"
            "-----------------------------------------\n\n"
        )
        recipient_email = 'vishwakarmamechfab.in@gmail.com'

        send_mail(subject, email_message, email, [recipient_email])

        return HttpResponse("Thank you,for contact us, Your message has been sent.(we will contact you soon)")
                # return render(request,'HOME.html')
    return render(request, 'vm.html') 