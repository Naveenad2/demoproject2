from django.db import models

# Create your models here

class Lecture_category(models.Model):


    catogory_name = models.CharField(max_length=100)
    catogory_discription = models.TextField(max_length=100)
    catogory_photo = models.ImageField(upload_to='./static/images')

    def __str__(self) :
        return self.catogory_name


class Video(models.Model):
    Video_name = models.CharField(max_length=100)
    Video_discription = models.TextField(max_length=500)
    video_image = models.ImageField(upload_to='./static/images')

    Choose_catogory = models.ForeignKey(Lecture_category,
                                       on_delete=models.CASCADE)

    Choose_video= models.FileField(upload_to='./static/vedio')
   

class Edit_Home_Page(models.Model):

    Main_heading = models.CharField(max_length=100)
    Discription = models.TextField(max_length=700)
    Main_photo = models.ImageField(upload_to='./static/images')
