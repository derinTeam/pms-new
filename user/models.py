from django.db import models
from django.contrib.auth.models import User
from project.models import Projects
# Create your models here.

class Comment(models.Model):
    project = models.ForeignKey(Projects,on_delete = models.CASCADE,verbose_name = "Proje",related_name= "comments")
    comment_author = models.CharField(max_length=50,verbose_name = "Yorum Yazarı")
    comment_content = models.CharField(max_length=200,verbose_name = "Yorum Alanı")
    comment_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.comment_content
    
    class Meta:
        ordering = ['-comment_date'] 