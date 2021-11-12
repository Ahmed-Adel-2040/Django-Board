from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board( models.Model ):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=150)
    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_date').first()


class Topic( models.Model ) :
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(Board,related_name="topics",on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    Views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

class Post( models.Model ) :
    massage = models.TextField(max_length=40000)
    topic = models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User,related_name='+',null=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.massage


