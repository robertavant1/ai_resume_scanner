from django.db import models

class Resume(models.Model):
    # Basic Information
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    resume_file = models.FileField(upload_to='resumes/')  
    experience = models.TextField(blank=True, null=True)  

    education = models.TextField(blank=True, null=True)  

    skills = models.TextField(blank=True, null=True) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="experiences")
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
    
class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="educations")
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"

class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_description = models.TextField()
    required_skills = models.TextField(blank=True, null=True)  
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company_name}"

class ResumeAnalysis(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, related_name="analysis")
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name="matched_resumes", blank=True, null=True)
    match_percentage = models.FloatField()  # 
    missing_skills = models.TextField(blank=True, null=True) 
    suggested_improvements = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Analysis for {self.resume.full_name} - {self.match_percentage}% match"
