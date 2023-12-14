from django.shortcuts import render
from app.models import *
# Create your views here.

def display_tables(request):
    ETOO=EmployeeTable.objects.all()
    d={'topics':ETOO}
    return render(request,'display_tables.html',d)

