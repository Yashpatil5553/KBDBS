from django.shortcuts import render, redirect
from .models import currencystate
from .utils import *
from django.contrib import messages


def sheetprocess(request):
    return render(request, 'process.html')

def vouchergen(request):
    return render(request, 'voucher.html')

    
def CMHome_page(request):
    bal_result = display_bal()  # Call the function to get the currency data

    if "message" in bal_result:
        return render(request, 'cmhome.html', {'message': bal_result["message"]})
    
    # Pass the results to the template
    return render(request, 'cmhome.html', {
        'denomination_details': bal_result['denomination_details'],
        'total_balance': bal_result['total_balance'],
        'total_notes': bal_result['total_notes']
    })


def updatebalance(request):
    bal_result = display_bal()
    # Fetch the object with id=1
    currency = currencystate.objects.get(id=1)
    
    if request.method == "POST":
        # Update the fields with the submitted values
        currency.fivehundred = request.POST.get("fivehundred", currency.fivehundred)
        currency.twohundred = request.POST.get("twohundred", currency.twohundred)
        currency.onehundred = request.POST.get("onehundred", currency.onehundred)
        currency.fifty = request.POST.get("fifty", currency.fifty)
        currency.twenty = request.POST.get("twenty", currency.twenty)
        currency.ten = request.POST.get("ten", currency.ten)
        currency.five = request.POST.get("five", currency.five)
        currency.two = request.POST.get("two", currency.two)
        currency.one = request.POST.get("one", currency.one)
        
        # Save the updated object to the database
        currency.save()
        messages.success(request, 'Currency state updated successfully!')
    
    return render(request, "update.html",{'currency': currency,
        'total_balance': bal_result['total_balance'],
        'total_notes': bal_result['total_notes']
    })  