from django.shortcuts import render
from yahoo_fin.stock_info import *



def stockpicker(request):
    picker = tickers_nifty50()
    print(picker)
    return render(request, 'main/stockpicker.html',{'picker':picker})


def stocktracker(request):
    details = get_quote_table('')
    return render(request,'main/stocktracker.html')
