from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.title


class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)
    items = models.ManyToManyField(MenuItem)

    def __str__(self):
        return self.name
