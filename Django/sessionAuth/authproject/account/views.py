import json                                                 # --> decode JSON
from django.http import JsonResponse                        # --> serialize to JSON
from django.middleware.csrf import get_token                # --> generate/retrive csrf Token
from django.views.decorators.csrf import ensure_csrf_cookie # --> send csrf token on GET request
from django.views.decorators.http import require_POST       # --> allows only on POST
from django.contrib.auth import authenticate, login, logout # --> Login authentication
from django.contrib.auth.decorators import login_required   # --> ensure if Login

# Get Csrf Token
@ensure_csrf_cookie
def get_csrf(request):
    token = get_token(request)
    return JsonResponse({'CsrfToken':token})

# Login logic
@require_POST
def login_view(request):
    # First Check whether the JSON response is valid or not
    try:
        data = json.loads(request.body.decode('utf-8'))
        print("PARSED JSON:", data)
    except Exception:
        return JsonResponse({'error':'invalid JSON'}, status=400)
    
    # Extract the username & Password
    username = data.get('username')
    password = data.get('password')

    # Check whether username & password exist 
    if not username or not password:
        return JsonResponse({'error':'username & password required'}, status=400)
    
    user = authenticate(request, username=username, password=password)
    # Checking If Credentials are valid
    if user is not None:
        login(request, user) # Session is stored
        return JsonResponse({'message':'Logged in', 'username': user.username})
    else:
        return JsonResponse({'error':'Invalid Credentials'}, status=401)
    
# Logout logic
@require_POST
def logout_view(request):
    logout(request)
    return JsonResponse({'message':'logged out'})

# Checking Protection
@login_required
def protected_view(request):
    return JsonResponse({'message':f'{request.user.username}, Is Authenticated'})