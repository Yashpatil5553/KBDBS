from django.shortcuts import render
# Create your views here.
def formhome_page(request):
    return render(request, 'formhome.html')

def form_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        code = request.POST.get("code")
        total_rpm = float(request.POST.get("total_rpm"))
        total_team = float(request.POST.get("total_team"))
        year_sales = float(request.POST.get("year_sales"))
        last_year_sales = float(request.POST.get("last_year_sales"))
        last_year_income = float(request.POST.get("last_year_income"))
        last_year_team = float(request.POST.get("last_year_team"))
        this_year_income = float(request.POST.get("this_year_income"))
        this_year_sales = float(request.POST.get("this_year_sales"))
        this_year_team = float(request.POST.get("this_year_team"))

        # Calculations
        registration = (total_rpm / total_team)*100
        repurchase = year_sales / total_rpm
        team_performance = (year_sales / total_team) / 500

        # Determine Registration Level
        if registration < 4:
            reg_status = "Bad😞"
        elif 4 <= registration <= 6:
            reg_status = "Average😐"
        elif 7 <= registration <= 10:
            reg_status = "Good🙂"
        else:
            reg_status = "Awesome😃"

        # Determine Repurchase Level
        if repurchase < 4000:
            rep_status = "Bad😞"
        elif 4000 <= repurchase <= 7000:
            rep_status = "Average😐"
        elif 7000 <= repurchase <= 11000:
            rep_status = "Good🙂"
        else:
            rep_status = "Awesome😃"

        # Determine Team Performance Level
        if team_performance < 4:
            team_perf_status = "Bad😞"
        elif 4 <= team_performance <= 6:
            team_perf_status = "Average😐"
        elif 6 <= team_performance <= 12:
            team_perf_status = "Good🙂"
        else:
            team_perf_status = "Awesome😃"

        # Income Target Calculation
        this_year_sales_income = (last_year_sales / last_year_income) * this_year_income
        this_year_team_income = (last_year_team / last_year_income) * this_year_income

        # Sales Target Calculation
        this_year_income_sales = (last_year_income / last_year_sales) * this_year_sales
        this_year_team_sales = (last_year_team / last_year_sales) * this_year_sales

        # Team Target Calculation
        this_year_income_team = (last_year_income / last_year_team) * this_year_team
        this_year_sales_team = (last_year_sales / last_year_team) * this_year_team

        return render(request, "result.html", {
            "name": name,
            "code": code,
            "registration": registration,
            "reg_status": reg_status,
            "repurchase": repurchase,
            "rep_status": rep_status,
            "team_performance": team_performance,
            "team_perf_status": team_perf_status,
            "this_year_sales_income": this_year_sales_income,
            "this_year_team_income": this_year_team_income,
            "this_year_income_sales": this_year_income_sales,
            "this_year_team_sales": this_year_team_sales,
            "this_year_income_team": this_year_income_team,
            "this_year_sales_team": this_year_sales_team,
            "this_year_income" : this_year_income,
            "this_year_sales" : this_year_sales,
            "this_year_team" : this_year_team,
        })

    return render(request, "formpg.html")