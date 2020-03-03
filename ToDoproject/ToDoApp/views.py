from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Taskinfo
from .forms import TaskForm

def index(request): 
    
    if request.method == 'POST':
        form = TaskForm(request.POST or None) 
        print("POST Method")
        #To check the user input uncomment the below lines.
        '''taskname = request.POST['task_name']
        taskcategory = request.POST['task_category']
        task_starttime = request.POST['start_time']
        task_endtime =request.POST['end_time']
        task_repeat = request.POST['task_repeatative']
        taskstatus = request.POST['task_status']
        print(form.errors)'''

        if form.is_valid(): 
            print(request.POST) #To see the Post data
            if Taskinfo.objects.filter(task_name = form.cleaned_data['task_name']).exists() :
                messages.warning(request,"Task with the same name already exists!!!")
            else:
                form.save()      
                messages.success(request,"Task added. Please check under My Tasks")
        else:
            messages.error(request, "Looks like you missed something. Please add the task again...")
                   
        return HttpResponseRedirect("/")
    
    else:
        form = TaskForm()
        print("GET MEthod")
        user_input = Taskinfo.objects.all()  #This is to display all the user ToDos

    return render(request, "ToDoApp/index.html", {'form':form, 'user_input':user_input}) 
