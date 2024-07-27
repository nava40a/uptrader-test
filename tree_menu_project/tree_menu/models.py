from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        related_name='items',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return self.url

    def __str__(self):
        return self.name
