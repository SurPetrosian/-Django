from django.db import models

class Blog(models.Model):
    header = models.CharField(max_length=300, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое', null=True, blank=True)
    image = models.ImageField( verbose_name='изображение',null=True, blank=True)
    created_at = models.DateField(verbose_name='дата создания')
    is_published = models.BooleanField(default=False)
    number_of_views = models.BigIntegerField(verbose_name='количество просмотров',default=0)


    def __str__(self):
        return self.header



    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ['header',]



