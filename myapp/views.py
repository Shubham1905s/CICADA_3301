from django.shortcuts import render, redirect
# import json
# from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import GamePassword, ResultTeam

# Create your views here.
# def home(request):
#     return render(request,'home.html')


def home(request):
    if request.method == "POST":
        team_name = request.POST.get('team_name')
        password = request.POST.get('password')

        # Check if the password matches
        try:
            game_password = GamePassword.objects.get(correct_password=password)
            # Store the team name in ResultTeam model if password is correct
            ResultTeam.objects.create(team_name=team_name)
            return redirect('myapp:results')  # Redirect to results.html page
        except GamePassword.DoesNotExist:
            return render(request, 'home.html', {'error': 'Incorrect password'})

    return render(request, 'home.html')

def About(request):
    return render(request,'About.html')

def results(request):
    return render(request,'results.html')