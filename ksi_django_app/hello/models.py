from django.db import models
from django.utils.text import slugify
from ksi_django_app.validators import title_val

# Create your models here.
class Posr(models.Model):
    title = models.CharField(max_length=20, validators= [title_val])
    body = models.TextField()
    email = models.EmailField(blank=True)
    slug = models.SlugField(blank=True, editable=False)
    
    def save(self):
        self.slug = slugify(self.title)
        super(Posr, self).save()
    
    # def __str__(self):
    #     return "{}".format(self.title)
    
