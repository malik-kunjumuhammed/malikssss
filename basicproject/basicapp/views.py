from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import place1
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=place1.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

# def about(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res1=x-y
#     res2=x*y
#     res3=x/y
#     return render(request,"contact.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})


















# def contact(request):
#     return render(request,"contact.html")
#
# def detail(request):
#     return HttpResponse("am detail")
#
# def thanx(request):
#     return render(request,"thanx.html")


