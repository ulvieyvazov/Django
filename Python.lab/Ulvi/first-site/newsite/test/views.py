# from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render



# Create your views here.


def index(request):
    return render(request, 'Ulvi/index.html')



def about(request):
    return render(request, "Ulvi/about.html")





# def about(request):
#     return render(request,'Ulvi/about.html')



# def index1(request):
#     return render(request, 'Ulvi/index1.html', context = {"body": "<h1>Hello World!</h1>"})


# def index(request):
#     data={'title':'Əsas Səhifə', 'header':'Hello Django','message':'Welcome to Python'}
#     return render(request,'Ulvi/index.html',context=data)



# def index(request):
#     return HttpResponse("Esas sehife")

# def about(request):
#     return HttpResponse("Sayt haqqinda")

# def contact(request):
#     return HttpResponse("Elaqe")

# def blog(request):
#     return HttpResponse("Blog")

# def user(request,name,age):
#     return HttpResponse(f"<h2>Name: {name} Age:{age}<h2/>")

# def archive(request,year):
#     return HttpResponse(f'<h1>Illə bağlı arxiv</h1><p>{year}</p>')

# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1>Səhifə tapılmadı</h1>')
