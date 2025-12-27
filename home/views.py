from django.shortcuts import render #type: ignore



def home(request): #type: ignore
    print('home')

    context = {'text': 'Olá home'}
    
    return render(
        request, #type: ignore
        'home/index.html', 
        context,
        )

