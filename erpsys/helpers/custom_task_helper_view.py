# from rest_framework.decorators import api_view
from django.shortcuts import render
from erpsys.forms.custom_task_form import CustomTaskForm


def custom_task(request):
    if request.method == "GET":
        form = CustomTaskForm()
        return render(request,"custom_task_template.html",context={
            "form":form
        })
    else:
        input_ids = request.POST['item_ids']
        auth_key = request.POST['authorization_key']
        input_id_spit_arr = input_ids.split('\r\n')
        response = get_response(input_id_spit_arr,auth_key)
        return render(request,'custom_task_template.html',context={'output':response})
        # return render(request,"custom_task_template.html",)



def get_response(item_ids,auth_key):
    import requests
    from decouple import config
    import json
    api_key = "Bearer"+auth_key
    url = "https://belkp.cga.omnib.manh.com/inventory/api/ServiceDefinition/invoke/findCacheDiscrepancy"
    headers = {
        "Authorization":api_key,
        "Content-Type" : "application/json"
    }
    invaid_item_ids = []
    valid_item_ids = []
    responses = []
    for item in item_ids:
        payload = {
            "SupplyRequestList": [
                {
                    "ViewId": "361cdadf-b5d4-414b-aeca-b77c99312590",
                    "Items": [
                        str(item),
                    ]
                    }
                ]
            }
        req_payload = json.dumps(payload)
        response = requests.post(url=url,headers=headers,data=req_payload)
        # print(response.json())
        res = response.json()
        result = get_result_from_response(res)
        responses.append({'item':item,'response':res['data']})
        if not result:
            invaid_item_ids.append(item)
        else:
            valid_item_ids.append(item)
        # break
    return {'invalid_item_ids':invaid_item_ids,'valid_item_ids':valid_item_ids,'responses':responses}
    

def get_result_from_response(response):
    data_db_values = response['data']['DBValues']
    data_cache_values = response['data']['CacheValues']
    # print("***********")
    # print(data_db_values)
    for key,value in data_db_values.items():
        if str(int(value)) != '-999':
            return False
    for key,value in data_cache_values.items():
        if str(int(value)) != '0':
            return False
        
    return True