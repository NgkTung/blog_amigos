from django.contrib import admin
from cloudinary.forms import CloudinaryFileField
from cloudinary import uploader
from cloudinary.exceptions import Error
from django.db import models
from slugify import slugify

from .models import Post, Tag


def delete_image(public_id):
    try:
        uploader.destroy(public_id)
        print(f"Image with public ID '{public_id}' deleted successfully.")
    except Error as e:
        print(f"Error deleting image with public ID '{public_id}': {str(e)}")


# Post Admin Panel
class PostAdmin(admin.ModelAdmin):
    # Change the image upload field to a Cloudinary upload field
    formfield_overrides = {
        models.ImageField: {'widget': CloudinaryFileField},
    }
    readonly_fields = ('slug',)  # Readonly fields
    exclude = ['click_count']  # The click count will be set to a default value of 0 when the post is created

    def save_model(self, request, obj, form, change):
        if change and 'image' in form.changed_data:
            # Save the new image to Cloudinary
            result = uploader.upload(obj.image)

            # Delete the old image if it exists
            existing_obj = Post.objects.get(pk=obj.pk)
            if existing_obj.image and hasattr(existing_obj.image, 'public_id'):
                public_id = existing_obj.image.public_id
                uploader.destroy(public_id)
                print("Old image has detroyed")

            # Update the image field with the new secure URL
            obj.image = result.get('secure_url', '')

        if not obj.slug_title:  # Generate slug_title default only if it doesn't exist
           obj.slug_title = obj.title[:50]

        if not obj.slug:
            obj.slug = slugify(obj.slug_title)

        if change and obj.slug_title != obj.slug:
            base_slug = slugify(obj.slug_title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(id=obj.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            obj.slug = slug

        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        # Delete associated image from Cloudinary
        if obj.image and hasattr(obj.image, 'public_id'):
            public_id = obj.image.public_id
            uploader.destroy(public_id)

        # Call the default delete_model method to delete the object
        super().delete_model(request, obj)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
