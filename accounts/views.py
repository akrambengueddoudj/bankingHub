from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile, PayementRecipe, Message


def signup(request):
    fname = None
    lname = None
    username = None
    password = None
    email = None
    phone = None
    address = None
    if request.method == 'POST' and 'registerfreebtn' in request.POST:
        if 'fname' in request.POST:
            fname = request.POST['fname']
        if 'lname' in request.POST:
            lname = request.POST['lname']
        if 'username' in request.POST:
            username = request.POST['username']
        if 'password' in request.POST:
            password = request.POST['password']
        if 'email' in request.POST:
            email = request.POST['email']
        if 'phone' in request.POST:
            phone = request.POST['phone']
        if 'address' in request.POST:
            address = request.POST["address"]

    if fname and lname and username and password and email and phone and address:
        if User.objects.filter(username=username).exists():
            return JsonResponse({"message": "Username already exists.", 'code': 1})
        else:
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "Email already used.", 'code': 2})
            else:
                user = User.objects.create_user(
                    username=username, password=password, first_name=fname, last_name=lname)
                user.save()
                userProfile = UserProfile(
                    user=user, phone_number=phone, address=address)
                userProfile.save()
                # login  the new user
                auth.login(request, user)
                return JsonResponse({"message": "User created", 'code': 3})
    else:
        return JsonResponse({"message": "Fill All data", 'code': 4})


def signin(request):
    message = ""
    context = {}
    code = -1
    username = None
    password = None
    if request.method == 'POST' and 'signinbtn' in request.POST:
        if 'username' in request.POST:
            username = request.POST['username']
        if 'password' in request.POST:
            password = request.POST['password']
    if username and password:
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                message = "Logged In Successfully."
                code = 0
            else:
                message = "Your account is disabled."
        else:
            message = "Invalid username or password."
        context = {"message": message, 'code': code}
    else:
        context = {
            "message": "Please enter  your username and password.", 'code': 2}
    return JsonResponse(context)


def logout(request):
    auth.logout(request)
    return redirect('home')


def confirm_payement(request):
    image = None
    type = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'image' in request.FILES:
                image = request.FILES['image']
            if 'type' in request.POST:
                type = request.POST['type']
        if image and type:
            payement_recipe = PayementRecipe(
                user_profile=request.user.userprofile, image=image, recipe_type=type)
            payement_recipe.save()
            return JsonResponse({'message': "Payement Added", 'code': 0})
        return JsonResponse({'message': "Fill all data", 'alldata': [str(image), type], 'post': request.POST, 'code': 1})
    else:
        return JsonResponse({'message': "You are not logged in", 'code': 2})


def message_us(request):
    code = -1
    messageResponse = ""
    full_name = None
    email = None
    subject = None
    phone = None
    message = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'full_name' in request.POST:
                full_name = request.POST['full_name']
            if 'email' in request.POST:
                email = request.POST['email']
            if 'subject' in request.POST:
                subject = request.POST['subject']
            if 'phone' in request.POST:
                phone = request.POST['phone']
            if 'message' in request.POST:
                message = request.POST['message']
        if message is not None and full_name is not None and email is not None and subject is not None and phone is not None:
            messageus = Message(user=request.user, full_name=full_name,
                                email=email, subject=subject, phone=phone, message=message)
            messageus.save()
            code = 0
            messageResponse = "Message Sent Successfully"
    return JsonResponse({'message': messageResponse, 'code': code})
