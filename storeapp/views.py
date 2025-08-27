from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from storeapp.models import Contacts,Featured_houses,blog
from django.contrib import messages
# Create your views here.

def index(request):
        
    if request.method == "POST":
        name = request.POST.get('text')
        email = request.POST.get('email')
        subject = request.POST.get('Subject')
        message = request.POST.get('message')
        contact = Contacts(name=name, email=email, subject=subject, message=message)
        contact.save()

        return redirect('/home')  # Redirect to the same page or another page after submission
    else:
        phone = '0714980899'
        context = {'phone': phone}

        return render(request,'index.html',context)
def starter(request):
     
    return render(request,'starter.html')
def home(request):
     feature = Featured_houses.objects.all()
    
     return render(request,'home.html',{'featured':feature})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if password == password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                # Store the full name
                user.first_name = username  # You could split the name into first_name and last_name if needed
                user.save()

                messages.success(request, 'Account created successfully!')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')  # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    
@login_required
def dashboard(request):
    user_name = request.user.username
    listing = Featured_houses.objects.count()
    context = {'user_name': user_name,
               'listing': listing
               }
    
    return render(request, 'dashboard.html', context)
  
def blog_view(request):
    blogs = blog.objects.all() # Fetch all blog posts, ordered by creation date
    return render(request, 'blog.html', {'blogs': blogs})