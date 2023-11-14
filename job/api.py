from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

#Endpoint for get all jobs from job model from django
@api_view(['GET'])
def joblistapi(request):
    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs, many=True).data
    
    return Response({"data": data})

@api_view(['GET'])
def job(request, pk=None):
    job = Job.objects.get(pk=pk)
    data = JobSerializer(job).data

    return Response({"data": data})