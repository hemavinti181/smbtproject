from django.shortcuts import render, redirect
import requests
import json
# Create your views here.
def index(request):
    return render(request,'base.html')

def login(request):

        if request.method == 'POST':
            url = "http://13.127.133.6/token"

            payload = {'username': request.POST.get('username'),
                       'password':  request.POST.get('password')}
            files = [

            ]
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload, files=files)

            print(response.text)
        return render(request, 'masters/login.html')

def unit_master(request):
    if request.method == 'POST':
        url = "http://13.127.133.6/ADD USER MASTER_NEW_UNIT"

        payload = {
                   'unit_code': request.POST.get('unitcode'),
                   'unit_name': request.POST.get('unitname'),
                   'cluster_name': request.POST.get('cluster'),
                   'address': request.POST.get('address'),
                   'status': request.POST.get('status'),
                    'files':request.POST.get('file')}

        headers = {
            'Authorization': 'bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDAxIiwiZXhwIjoxNjczOTUzNzc2fQ.QFF5HS7CaSd5HayGe5Rv3mOEmEZu4eYv-b72GVdC0NgsqPWGJPXXMPqmJuJUQgz6HKaxGfrz1RF-oSMOoTA9-g'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        data=response.json()
    return render(request,'masters/unit_master.html')

def cluster_master(request):

    return render(request,'masters/cluster_master.html')

def user_master(request):
    return render(request,'masters/user_master.html')

def state_master(request):
    url = "http://13.127.133.6/State List?country_code=AF"

    payload = {}
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDAxIiwiZXhwIjoxNjczNTEzMzQ2fQ.LdedkvcUv7CEZVS3lzUjzEnYsyG3noWplZuCgPkdTEDcqCXciVyd1TgRIPKB-vGb5IzPMxLY75zPPuDh50pZmQ'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data=response.json()
    data=data['State List']
    return render(request,'masters/state_master.html',{'data':data})

def country_master(request):
    url = "http://13.127.133.6/Country List"

    payload = {}
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDAxIiwiZXhwIjoxNjczNTEzMzQ2fQ.LdedkvcUv7CEZVS3lzUjzEnYsyG3noWplZuCgPkdTEDcqCXciVyd1TgRIPKB-vGb5IzPMxLY75zPPuDh50pZmQ'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    data = data['Country List']
    return render(request,'masters/country_master.html',{'data':data})

def role_master(request):
    return render(request,'masters/role_master.html')

def revenue_targets(request):
    return render(request,'masters/revenue_targets.html')

def admission_targets(request):
    return render(request,'masters/admission_targets.html')

def report_calls(request):
    return render(request,'callmanagement/report_calls.html')

def report_activity(request):
    return render(request,'callmanagement/report_activity.html')

def masterlist(request):
    return render(request,'callmanagement/masterlist.html')

