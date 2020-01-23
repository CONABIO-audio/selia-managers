from django.shortcuts import render

def management(request):
  # context = {}
  return render(request, 'selia_managers/management.html')
