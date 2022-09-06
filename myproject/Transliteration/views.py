from unittest import result
from urllib import response
from webbrowser import get
from django.shortcuts import render , redirect
from .models import Trans
from .Transliteration_Function import Transliteration
import csv 
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
def home(request):
    if request.method=='POST':
        noun=request.POST ['noun']
        return redirect(f'/result/{noun}')
    return render(request,'Transliteration/home.html')

def after (request,noun):
    data=Trans.objects.filter(Noun__icontains=noun)
    print(data)
    result_list =[]
    if data is not None:
        for res in data :
            result_list.append(
                {
                'Noun':Transliteration(res.Noun),
                 'Adress':Transliteration(res.Adress),
                'Nationality':Transliteration(res.Nationality),
                'Place_of_birth':Transliteration(res.Place_of_birth), 
                'Datebirth':res.Datebirth,
                }
            )
    print(result_list)
    return render(request,'Transliteration/result.html',{'data':result_list})
   
    
def Downloadcsv(request,noun):
    response= HttpResponse(content_type='text/csv')
    cd ='attachment;filename="{0}"'.format('result_list.csv')
    response['Content-Disposition'] =cd 
    
    writer =csv.writer(response)
    data=Trans.objects.filter(Noun__icontains=noun)
    result_list =[]
    if data is not None:
        for res in data :
            result_list.append([
                Transliteration(res.Noun),
                res.Datebirth,
                Transliteration(res.Adress),
                Transliteration(res.Nationality),
                Transliteration(res.Place_of_birth),
                ])
                
               
                
    writer.writerow(['Noun','Date_of_Birth','Adress','Nationality','Place_of_birth'])
    list=result_list
    for t in list:
        writer.writerow(t)
    return response
    
