from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Followrs
import csv

def export_csv(request):
    students=Followrs.objects.all()
    response=HttpResponse('text/cvs')
    response['Content-Disposition'] = 'attachment; filename=export_csv' + str(datetime.now()) + '.csv'

    write=csv.writer(response)
    write.writerow([ 'id',  'name', "email"])   ##### madel ni ichidagini yozamz
    students_fields=students.values_list('id', 'name', 'email')
    for student in students_fields:
        write.writerow(student)
    return response

# def home_page(request):    #### new 1
#
#     # if request.POST:      ## new 3
#     #     model=Followrs()     ##### new 5 obeck olyapmz
#     #     model.email=request.POST.get("email", "")   ### new 6
#     #     model.save()   #### new 7
#
#     if request.POST:      ## new 3
#         model=Followrs()     ##### new 5 obeck olyapmz
#         email, name=request.POST.get("email", None),request.POST.get("name", None) #, request.POST.get("number", None)  ### new 6
#         if email:
#             model.email = email
#         elif name:
#             model.name=name
#         # elif number:
#         #     model.number = number
#         else:
#             model.email=None,
#             model.name=None
#
#         model.save()   #### new 7
#         #print(request.POST)       ### new 4
#     return render(request, 'index.html')   ### new 2

def home_page(request):
    if request.method == 'POST':
        model = Followrs()
        model.email = request.POST.get('email')
        model.name = request.POST.get('name')
        model.phone = request.POST.get('phone')

        model.save()

        return render(request,'index.html')
    else:
        return render(request,'index.html')




