from django.contrib import admin
from cloudinary.forms import CloudinaryFileField
from cloudinary import uploader
from django.db import models

from .models import Post, Tag


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': CloudinaryFileField}
    }

    def save_model(self, request, obj, form, change):
        if change and 'image' in form.changed_data:
            # Save the new image to Cloudinary
            result = uploader.upload(obj.image)

            # Delete the old image if it exists
            existing_obj = Post.objects.get(pk=obj.pk)
            if existing_obj.image and hasattr(existing_obj.image, 'public_id'):
                public_id = existing_obj.image.public_id
                uploader.destroy(public_id)

            # Update the image field with the new secure URL
            obj.image = result.get('secure_url', '')

        super().save_model(request, obj, form, change)


admin.site.register(Post, MyModelAdmin)
admin.site.register(Tag)
