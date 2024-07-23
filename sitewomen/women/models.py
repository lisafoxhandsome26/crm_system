from django.db import models as md


class Women(md.Model):
    title = md.CharField(max_length=255)
    content = md.TextField(blank=True)
    time_create = md.DateTimeField(auto_now_add=True)
    time_update = md.DateTimeField(auto_now=True)
    is_published = md.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            md.Index(fields=['-time_create'])
        ]