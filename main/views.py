from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406424190',
        'name': 'Muhammd Haikal',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)