from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task

# ---list views to create same project----
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

# ---list view difine using class ---

class  Tasklistview(ListView):
    model=Task
    # indexpage
    template_name = 'home.html'
    # variable name in home page
    context_object_name = 'tsk'

class Taskdetailview(DetailView):
    model =Task
    template_name = 'detail.html'
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update1.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class Taskdeleteview(DetailView):
     model = Task
     template_name = 'delete.html'
     success_url=reverse_lazy('cbvhome')






# Create your views here.
def home(request):
    task2 = Task.objects.all()
    # add feild
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        # fech data in db
        task1=Task(name=name,priority=priority,date=date)
        task1.save()
    #     -----end fld
    return render(request,"home.html",{'tsk':task2})
# detail page

# def details(request):
#     task2=Task.objects.all()
#     return render(request,'detail.html',{'tsk':task1})

# delete function
def delete(request,taskid):
    # fetch datas
    task2=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task2.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    tsk=Task.objects.get(id=id)
    # form fetch
    f=TodoForm(request.POST or None,instance=tsk)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'tsk':tsk})