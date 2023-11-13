from django.shortcuts import redirect, render
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm, JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

def job_list(request):
    jobs = Job.objects.all()
    filters = JobFilter(request.GET, queryset=jobs)
    jobs = filters.qs    
    paginator = Paginator(jobs, 5)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)
    context = {'jobs': page_obj, "filters":filters}
    
    return render(request, 'job/jobs.html', context)



def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm()
    return render(request, 'job/job_details.html', {'job_detail': job_detail, 'form': form})


@login_required
def add_job(request):
    job_owner = request.user
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = job_owner
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()
    return render(request, 'job/add_job.html', {'form': form})