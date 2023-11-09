from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm

def job_list(request):
    jobs = Job.objects.all()   
    paginator = Paginator(jobs, 1)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)

    return render(request, 'job/jobs.html', {'jobs': page_obj})



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

