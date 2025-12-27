from django.shortcuts import render #type: ignore


def blog(request): #type: ignore
    print('blog')

    context = {
        'text': 'BLOG PAGE',
        'title': 'Página de exemplo - '          
               }

    return render(
        request, #type: ignore
        'blog/index.html',
        context,
        )


def exemplo(request):#type: ignore
    print('exemplo')

    context = {'text': 'Olá, Exemplo'}

    return render(
            request, #type: ignore
            'blog/exemplo.html',
            context
            )
