from django.db import models

# Create your models here.
class State(models.Model):
    value = models.CharField(max_length=32, default='initial')
    
    def save(self, *args, **kwargs):
        print('saved')
        super(State, self).save(args, **kwargs)