from django.db import models
from django.contrib import messages
from tinymce import models as tinymce_models
from cloudinary.models import CloudinaryField
from slugify import slugify

class Tag(models.Model):
    # Name of tag
    name = models.CharField(max_length=30)
    # Description for more information this tag about
    description = models.TextField(
        max_length=400, default='This tag has no description yet!')
    # URL name for django routing
    url_name = models.CharField(max_length=30)
    # Some tag maybe sub tag, so they will have parent_tag
    parent_tag = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        parent_name = self.parent_tag.name if self.parent_tag else ""
        return f"{parent_name} | {self.name}"


class Post(models.Model):
    # Titlte of post
    title = models.CharField(max_length=100, unique=True)
    # Some small information to introduce viewers to click the post
    description = models.CharField(
        max_length=250, default='This post has no description yet!')
    # Main image 
    image = CloudinaryField('image')
    # Body of post
    content = tinymce_models.HTMLField(default="This post has no content")
    # Post has more than 1 tag
    tag = models.ManyToManyField(Tag)
    # Created date time
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    # To determine the number of times this post has been clicked on
    click_count = models.PositiveIntegerField(default=0)
    # To form url for page instead of id
    slug_title = models.CharField(blank=True, max_length=50)
    # URL for page
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    # Update click_count when post has clicked
    def increment_click_count(self):
        self.click_count += 1
        self.save()

    def word_count(self):
        content_words = self.content.split()
        return len(content_words)

    # Custome save post method
    def save(self, *args, **kwargs):
        if not self.slug_title: # Generate slug_title default only if it doesn't exist
            base_slug_title = self.title[:50]
            if Post.objects.filter(slug=slugify(base_slug_title)).exists:
                messages.error(None, "Slug title existed!")
                return
            else: 
                self.slug_title = base_slug_title

        # Update the slug field when slug_title changes
        if self.id and self.slug_title != self.slug:
            base_slug = slugify(self.slug_title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        if not self.slug:  # Generate slug only if it doesn't exist
            base_slug = slugify(self.slug_title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        # To ensure that the click_count cannot go below 0
        if self.click_count < 0:
            self.click_count = 0
        super(Post, self).save(*args, **kwargs)
