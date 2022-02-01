from django.db import models


class Search (models.Model):
    search = models.CharField(max_length=500)
    updated_at= models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)


    def __str__ (self):
        return self.search

    class Meta:
       
        verbose_name = 'Search'
        verbose_name_plural = 'Searches'
