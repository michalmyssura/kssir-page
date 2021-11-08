from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


def contact(request):
    request.method == 'POST'
    name = request.POST.get('name', '')
    message = request.POST.get('message', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    y = '\n'
    x = message + y + email + y + phone
    print(name, email, message, phone)
    if name and message and email:

        try:
            send_mail(name, x, email, ['kssir.konskie@gmail.com'], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, 'contact/contact.html')
    else:
        return render(request, 'contact/contact.html')



