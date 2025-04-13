from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    context=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author}\n{self.context}\n{self.created_date} - {self.updated_date}"
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk":self.pk})
