from django.db import  models



Job_TYPe=(
("full time","full time"),
("part time","part time"),


)
# Create your models here.
class job(models.Model):
    title= models.CharField(max_length=100)
    #location
    job_type=models.CharField(max_length=15,choices=Job_TYPe)
    description= models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancey=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    expr=models.IntegerField(default=1)
     

    def __str__(self) -> str:
         return self.title

