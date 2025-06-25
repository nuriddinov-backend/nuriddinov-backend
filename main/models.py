from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Status(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Index(models.Model):
    logo = models.ImageField(upload_to='index_logos/')
    title = models.CharField(max_length=255)
    text_projects = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class About(models.Model):
    photo = models.ImageField(upload_to='about_photos/')
    name1 = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255)
    text = models.TextField()
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.name1


class Projects(models.Model):
    photo = models.ImageField(upload_to='project_photos/')
    title = models.CharField(max_length=255)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='post_photos/')
    text = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Contact(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class Resume(models.Model):
    year = models.IntegerField()
    position = models.CharField(max_length=255)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.position


class SocialMedia(models.Model):
    photo = models.ImageField(upload_to='social_photos/')
    link = models.URLField()
    title = models.CharField(max_length=255)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    fullname = models.CharField(max_length=255)
    message = models.TextField()
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname