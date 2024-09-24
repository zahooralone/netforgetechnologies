from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Print debug information
        print(f"Attempting login for username: {username}")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('backendapp:dashboard')  # Redirect to the dashboard or desired page
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            # Return the login page with an error message
            return render(request, 'auth/login.html', {'error': 'Invalid username or password. Please try again.'})
        
    else:
        return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out successfully... \nThanks"))
    return redirect('login')

