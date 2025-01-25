from django.shortcuts import render, redirect
from .models import currencystate
from .utils import *
from django.contrib import messages
from django.http import FileResponse, HttpResponse
from .forms import UploadFileForm
from .utils import excel_to_db
from django.contrib.auth.decorators import login_required
from django.conf import settings
from pathlib import Path

@login_required(login_url='login')   
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

@login_required(login_url='login') 
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
        bal_result = display_bal()
    
    return render(request, "update.html",{'currency': currency,
        'total_balance': bal_result['total_balance'],
        'total_notes': bal_result['total_notes']
    })  


@login_required(login_url='login') 
def sheetprocess(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Step 1: Process the uploaded file and generate the Excel file
            uploaded_file = request.FILES['file']
            excel_file, excel_path = excel_to_db(uploaded_file)  # This will also call export_to_excel() internally
            
            if excel_file is None or excel_path is None:
                return HttpResponse("Error generating the Excel file.", status=500)

            # Step 2: Send the generated Excel file as a downloadable response
            response = HttpResponse(excel_file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={excel_path}'

            return response
    else:
        form = UploadFileForm()

    return render(request, 'process.html', {'form': form})

@login_required(login_url='login') 
def vouchergen(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Step 1: Process the uploaded Excel file and generate the .docx file
            uploaded_file = request.FILES['file']
            
            # Pass the binary file directly to CreateVoucher
            excel_file_bytes = uploaded_file.read()
            docx_file, docx_filename = CreateVoucher(excel_file_bytes)

            if docx_file is None or docx_filename is None:
                return HttpResponse("Error generating the document.", status=500)

            # Step 2: Send the generated .docx file as a downloadable response
            response = HttpResponse(docx_file, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename={docx_filename}'

            return response
    else:
        form = UploadFileForm()

    return render(request, 'voucher.html', {'form': form})


