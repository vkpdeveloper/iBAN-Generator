from django.http import HttpResponse
from django.shortcuts import render
from schwifty import IBAN

def index(request):
    return render(request, 'index.html')

def generate(request):
    country_code = request.POST.get('country', 'default')
    bank_code = request.POST.get('bkcode', 'default')
    account_code = request.POST.get('accode', 'default')
    print(country_code)
    print(bank_code)
    print(account_code)
    try:
        iban = IBAN.generate(country_code, bank_code=bank_code, account_code=account_code)
        parmas = {'iBAN_Goted':iban,}
    except ValueError:
        return render(request, 'error.html')
    else:
            return render(request, 'generate.html', parmas)
