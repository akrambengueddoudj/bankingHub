import random
from django.shortcuts import redirect, render
from django.http import JsonResponse
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from . import models


def index(request):
    return render(request, 'pages/index.html')


def statistics(request):
    return render(request, 'pages/statistics.html')


def about(request):
    return render(request, 'pages/about.html')


def islamic_banking(request):
    return render(request, 'pages/islamic_banking.html')


def loan_calculator(request):
    return render(request, 'pages/loan_calculator.html')


def banking_services(request):
    return render(request, 'pages/banking_services.html')


def stock_market(request):
    return render(request, 'pages/stock_market.html')


def fiscal_policy(request):
    return render(request, 'pages/fiscal_policy.html')


def monetary_policy(request):
    return render(request, 'pages/monetary_policy.html')


def electronic_banking(request):
    return render(request, 'pages/electronic_banking.html')


def loans(request):
    return render(request, 'pages/loans.html')


def deposits(request):
    return render(request, 'pages/deposits.html')


def algeria_bank(request):
    return render(request, 'pages/algeria_bank.html')


def banks_list(request):
    return render(request, 'pages/banks_list.html')


def banking_laws(request):
    return render(request, 'pages/banking_laws.html')


def open_bank_account(request):
    return render(request, 'pages/open_bank_account.html')


def general_info(request):
    return render(request, 'pages/general_info.html')


def financial_consulting(request):
    if request.user.is_authenticated:
        if request.user.userprofile.type == "p":
            consnultings = models.FinancialConsulting.objects.filter(
                user=request.user).order_by('-id')
            return render(request, 'pages/financial_consulting.html', {'consultings': consnultings})
    return redirect('home')


def reservation(request):
    if request.user.is_authenticated:
        if request.user.userprofile.type == "p":
            context = {'banks': models.Banks.objects.all(),
                       'branchs': models.BankBranch.objects.all(), 'cities': models.BankCity.objects.all()}
            return render(request, 'pages/reservation.html', context)
    return redirect('home')


def promotion(request):
    if request.user.is_authenticated:
        if request.user.userprofile.type == "b":
            return render(request, 'pages/promotion.html')
    return redirect('home')


def choose_bank(request):
    if request.user.is_authenticated:
        if request.user.userprofile.type == "p":
            return render(request, 'pages/choose_bank.html')
    return redirect('home')


def become_VIP(request):
    return render(request, 'pages/pricesVIP.html')


def recipe_VIP(request, type):
    if type == "client":
        price = 2000
    else:
        price = 20000
    return render(request, 'pages/recipeVIP.html', {'price': price, 'type': type})


def send_consulting(request):
    code = -1
    message = ""
    consulting = None
    if request.method == 'POST' and 'sendConsultingBtn' in request.POST:
        if request.user.is_authenticated:
            if request.user.userprofile.type == "p" or request.user.userprofile.type == "b":
                if 'consulting' in request.POST:
                    consulting = request.POST['consulting']
                    consultation = models.FinancialConsulting(
                        user=request.user, description=consulting)
                    consultation.save()
                    code = 0
                    message = "consulting sent"
    return JsonResponse({'message': message, 'code': code})


def set_reservation(request):
    code = -1
    message = ""
    bank = None
    branch = None
    city = None
    dateTime = None
    barcodeData = None
    if request.method == 'POST' and 'setReservationBtn' in request.POST:
        if request.user.is_authenticated:
            if request.user.userprofile.type == "p" or request.user.userprofile.type == "b":
                if 'bank' in request.POST:
                    try:
                        int(request.POST['bank'])
                        bank = request.POST['bank']
                    except ValueError:
                        pass
                if 'branch' in request.POST:
                    try:
                        int(request.POST['branch'])
                        branch = request.POST['branch']
                    except ValueError:
                        pass
                if 'city' in request.POST:
                    try:
                        int(request.POST['city'])
                        city = request.POST['city']
                    except ValueError:
                        pass
                if 'dateTime' in request.POST:
                    dateTime = request.POST['dateTime']
                if 'barcodeData' in request.POST:
                    barcodeData = request.POST['barcodeData']

            if bank is not None and branch is not None and city is not None and dateTime is not None and barcodeData is not None:
                if models.Banks.objects.filter(pk=int(bank)):
                    bank = models.Banks.objects.get(pk=int(bank))
                if models.BankBranch.objects.filter(id=int(branch)).exists():
                    branch = models.BankBranch.objects.get(pk=int(branch))
                if models.BankCity.objects.filter(id=int(city)).exists():
                    city = models.BankCity.objects.get(pk=int(city))
                reservation = models.Reservation(
                    user=request.user, bank=bank, branch=branch, city=city, date_time=dateTime)
                reservation.save()
                # Generate barcode
                barcode_img = BytesIO()
                code128 = barcode.get_barcode_class('code128')
                code = code128(barcodeData, writer=ImageWriter())
                code.write(barcode_img)

                # Save barcode image to model
                reservation.barcode_image.save(
                    f'{barcodeData}.png', barcode_img)
                code = 0
                message = "reservation added successfully"
            else:
                message = "fill all data"
        else:
            message = "authentication failure"
    else:
        message = "problem with method or button"
    return JsonResponse({'message': message, 'code': code, 'reservation': reservation.barcode_image.url})


def choose_correct_bank(request):
    choosed_bank = None
    code = -1
    message = ""
    if request.method == 'POST' and 'chooseBankBtn' in request.POST:
        if request.user.is_authenticated:
            if request.user.userprofile.type == "p" or request.user.userprofile.type == "b":
                total_banks = models.Banks.objects.count()

                # Generate a random index within the range of total products
                random_index = random.randint(0, total_banks - 1)

                # Get a random product using the generated index
                choosed_bank = models.Banks.objects.all()[random_index]
                code = 0
                message = "Bank choosed successfully"
            else:
                message = "problem with method or button"
    if choosed_bank is not None:
        return JsonResponse({'message': message, 'code': code, 'bankChoosed': choosed_bank.bank_name})
    return JsonResponse({'message': message, 'code': code})


def set_service(request):
    code = -1
    message = ""
    description = None
    if request.method == 'POST' and 'setServiceBtn' in request.POST:
        if request.user.is_authenticated:
            if request.user.userprofile.type == "b":
                if 'description' in request.POST:
                    description = request.POST['description']

        if description is not None:
            service = models.Service(
                user=request.user, description=description)
            service.save()
            if 'pictures' in request.FILES:
                pictures = request.FILES.getlist('pictures')
                for picture in pictures:
                    service_picture = models.ServicePictures(
                        service=service, picture=picture)
                    service_picture.save()
            code = 0
            message = "Service created successfully"
        else:
            message = "Description field can't be empty"
    else:
        message = "Problem with method or button"
    return JsonResponse({'message': message, 'code': code})


def new_services(request):
    services = models.Service.objects.prefetch_related('pictures')
    return render(request, 'pages/new_services.html', {'services': services})


def terms_of_use(request):
    return render(request, 'pages/terms_of_use.html')
