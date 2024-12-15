from django.shortcuts import render, redirect
from .models import DecisionOption
from .forms import DecisionOptionForm
import random

def home(request):
    categories = DecisionOption.objects.all()
    return render(request, 'decision_maker/home.html', {'categories': categories})

def category_options(request, category):
    options = DecisionOption.objects.filter(category=category)
    return render(request, 'decision_maker/category.html', {
        'category': category,
        'options': options
        
    })

def add_option(request):
    if request.method == 'POST':
        form = DecisionOptionForm(request.POST)
        if form.is_valid():
            form.save()  # Save new decision option
            return redirect('home')  # Redirect to home after saving
    else:
        form = DecisionOption()

    return render(request, 'decision_maker/add_option.html', {'form': form})

def coin_toss(request):
    result = random.choice(['Heads', 'Tails'])
    return render(request, 'decision_maker/coin_toss.html', {'result': result})





