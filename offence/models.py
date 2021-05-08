from django.db import models

class OffenceCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

    def offences(self):
        return Offence.objects.filter(offence=self).count()

    class Meta:
        verbose_name_plural = 'Offence Categories'
        
class Offence(models.Model):
    title = models.CharField(max_length=255)
    person_name = models.CharField(max_length=255)
    offence = models.ForeignKey(OffenceCategory, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    treated = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, verbose_name='date recorded')
    updated = models.DateTimeField(auto_now=True, verbose_name='last updated')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


