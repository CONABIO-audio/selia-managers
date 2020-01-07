from django.shortcuts import render


def management(request):
    return render(request, 'selia_managers/management.html')
