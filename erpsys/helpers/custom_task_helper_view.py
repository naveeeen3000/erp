from rest_framework.decorators import api_view
from django.shortcuts import render
from erpsys.forms.custom_task_form import CustomTaskForm

@api_view(['POST','GET'])
def custom_task(request):
    if request.method == "GET":
        form = CustomTaskForm()
        return render(request,"custom_task_helper_view.py",context={
            "form":form
        })
    form = CustomTaskForm(request.POST,request.FILES)
    if form.is_valid():
        file = form.files
    return render(request,'custom_task_helper.html',context={'file_data':file})