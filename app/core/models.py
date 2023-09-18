from django.db import models
from tinymce import models as tinymce_models
from cloudinary.models import CloudinaryField


class Tag(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(
        max_length=400, default='This tag has no description yet!')
    url_name = models.CharField(max_length=30)
    parent_tag = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        parent_name = self.parent_tag.name if self.parent_tag else ""
        return f"{parent_name} | {self.name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(
        max_length=250, default='This post has no description yet!')
    image = CloudinaryField('image')
    content = tinymce_models.HTMLField(default="This post has no content")
    tag = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
