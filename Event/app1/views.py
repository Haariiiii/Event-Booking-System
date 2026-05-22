from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Event,Booking
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.conf import settings
from .models import Event, Booking
from django.shortcuts import get_object_or_404, redirect




# Create your views here.
def home(request):
    return render(request,'home.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()

        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user is not None:
          login(request,user)
          return redirect('dashboard') 
        else:
            messages.error(request,"Invalid Username or password")

    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    events = Event.objects.all()
    booked_events = Booking.objects.filter(user=request.user).values_list('event_id', flat=True)

    return render(request, 'dashboard.html', {
        'events': events,
        'booked_events': booked_events
    })




@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if Booking.objects.filter(user=request.user, event=event).exists():
        messages.warning(request, "You already booked this event.")
    else:
        Booking.objects.create(user=request.user, event=event)

        # ✅ EMAIL MUST BE HERE (inside the function)
        send_mail(
            subject='Event Booking Confirmation',
            message=(
                f'Hi {request.user.username},\n\n'
                f'You have successfully booked "{event.title}".\n\n'
                f'Thank you for choosing Eventify!'
            ),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email],
            fail_silently=True,
        )

        messages.success(request, "Event booked successfully!")

    return redirect('dashboard')