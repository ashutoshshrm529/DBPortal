from django.shortcuts import render
from .models import DBer, User, City, State

import xlsxwriter
import xlrd
import datetime


def index(request):
    return render(request, 'DBers/index.html')


def addDBers(request):
    if request.method == "POST":
        excelfile = request.FILES["excelfile"]

        User.objects.filter(account_type='DBer').delete()

        wb = xlrd.open_workbook("test_upload.xlsx")
        sheet = wb.sheet_by_index(0)

        for row in range(1, 2):
            user = User.objects.get_or_create(first_name=sheet.cell_value(row, 0),
                                              last_name=sheet.cell_value(row, 1),
                                              email=sheet.cell_value(row, 2))
            dber = DBer.objects.get_or_create(user=User.objects.filter(email=sheet.cell_value(row, 2)).first(),
                                              aadhaar=sheet.cell_value(row, 3),
                                              dob=datetime.datetime(
                                                  *xlrd.xldate_as_tuple(sheet.cell_value(row, 4), wb.datemode)),
                                              gender=sheet.cell_value(row, 5),
                                              city=City.objects.filter(
                                                  name=sheet.cell_value(row, 6)).first(),
                                              state=State.objects.filter(name=sheet.cell_value(row, 7)).first())

        return render(request, 'DBers/index.html')
    else:
        return render(request, 'DBers/upload_sheet.html')
