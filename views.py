from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *


def landingview(request):
    template_name = 'index.html'
    return render(request, template_name)


def formview(request):
    template_name = 'test.html'
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print (form.cleaned_data)
            return HttpResponse('success')
    else:
        form = UserForm()
    return render(request, template_name, {'form': form})


def gender(request):
    index_1 = Company.objects.filter(sex='M', country='NGN').count()
    index_2 = Company.objects.filter(sex='M', country='GHN').count()
    index_3 = Company.objects.filter(sex='M', country='LBR').count()
    index_4 = Company.objects.filter(sex='M', country='SNG').count()
    country_male_set = [index_1, index_2, index_3, index_4]
    findex_1 = Company.objects.filter(sex='F', country='NGN').count()
    findex_2 = Company.objects.filter(sex='F', country='GHN').count()
    findex_3 = Company.objects.filter(sex='F', country='LBR').count()
    findex_4 = Company.objects.filter(sex='F', country='SNG').count()
    country_female_set = [findex_1, findex_2, findex_3, findex_4]
    return render(request, 'gender.html', {'male_set': country_male_set, 'female_set': country_female_set})


def product_rating(request):
    nindex_1 = Company.objects.filter(product_rating='R1', country='NGN').count()
    nindex_2 = Company.objects.filter(product_rating='R2', country='NGN').count()
    nindex_3 = Company.objects.filter(product_rating='R3', country='NGN').count()
    gindex_1 = Company.objects.filter(product_rating='R1', country='GHN').count()
    gindex_2 = Company.objects.filter(product_rating='R2', country='GHN').count()
    gindex_3 = Company.objects.filter(product_rating='R3', country='GHN').count()
    lindex_1 = Company.objects.filter(product_rating='R1', country='LBR').count()
    lindex_2 = Company.objects.filter(product_rating='R2', country='LBR').count()
    lindex_3 = Company.objects.filter(product_rating='R3', country='LBR').count()
    sindex_1 = Company.objects.filter(product_rating='R1', country='SNG').count()
    sindex_2 = Company.objects.filter(product_rating='R2', country='SNG').count()
    sindex_3 = Company.objects.filter(product_rating='R3', country='SNG').count()
    poor_country_set = [nindex_1, gindex_1, lindex_1, sindex_1]
    average_country_set = [nindex_2, gindex_2, lindex_2, sindex_2]
    good_country_set = [nindex_3, gindex_3, lindex_3, sindex_3]
    return render(request, 'product_rating.html', {'poor_set': poor_country_set, 'average_set': average_country_set,
                                                   'good_set': good_country_set})


def country_percentage(request):
    index_1 = Company.objects.filter(country='NGN').count()
    index_2 = Company.objects.filter(country='GHN').count()
    index_3 = Company.objects.filter(country='LBR').count()
    index_4 = Company.objects.filter(country='SNG').count()
    return render(request, 'country_max.html', {'index_1': index_1, 'index_2': index_2, 'index_3': index_3,
                                                'index_4': index_4})
