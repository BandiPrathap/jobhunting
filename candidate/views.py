from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from hr.models import JobPost , CandidateApplications
from candidate.models import MyApplyJobList
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required
def candidateHome(request):
    jobpost = JobPost.objects.all()
    return render(request,'candidate/dashboradh.html',{'jobpost':jobpost})



@login_required
def applyJob(request, id):
    if request.method == 'POST':
        # Retrieving form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        college = request.POST.get('college')
        passing_year = request.POST.get('passing_year')
        year_of_experience = request.POST.get('yearOfExperience')
        resume = request.FILES.get('resume')
        
        # Retrieving the job post object
        job = get_object_or_404(JobPost, id=id)
        
        # Checking if the candidate has already applied for this job
        if CandidateApplications.objects.filter(user=request.user, job=job).exists():
            return redirect('dash')  # Redirecting to dashboard if already applied
        
        job.applyCount += 1
        job.save()
        
        # Creating and saving a new instance for CandidateApplications model
        candidate_application = CandidateApplications.objects.create(
            user=request.user,
            job=job,
            passingYear=passing_year,
            yearOfExperience=year_of_experience,
            resume=resume
        )
        
        # Creating and saving a new instance for MyApplyJobList model
        existing_entry = MyApplyJobList.objects.filter(user=request.user, job=candidate_application).exists()
        if not existing_entry:
            # Create a new MyApplyJobList entry here
            my_apply_job_list = MyApplyJobList.objects.create(
                user=request.user,
                job=candidate_application
            )
        else:
            print("You have already applied!")
        
        return redirect('dash')  # Redirecting to dashboard after successful application submission
    
    # If request method is not POST, render the application form
    return render(request, 'candidate/apply.html')

@login_required
def myjoblist(request):
    joblist = MyApplyJobList.objects.filter(user=request.user).values()
    print( joblist)
    return render(request,'candidate/myjoblist.html',{'joblist':joblist})

