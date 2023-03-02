from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name='Menu name')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'


class MenuItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    url_name = models.CharField(max_length=100, verbose_name='Named URl')

    menu = models.ForeignKey(Menu, blank=True, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='childs', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def __str__(self):
        return str(self.title)
