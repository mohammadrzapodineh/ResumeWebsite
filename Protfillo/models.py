from django.db import models


class Portfillo(models.Model):
    title = models.CharField(max_length=110, verbose_name='عنوان نمونه کار')
    image = models.ImageField(verbose_name='تصویر نمونه کار', upload_to='images/portfiilo/images/')
    image_link = models.ImageField(verbose_name='عکس پیشنمایش پروژه در صورت داشتن', blank=True, null=True, upload_to='images/portfiilo/image_link/') 
    category = models.ManyToManyField('Category', verbose_name='دسته بندی نمونه کار', related_name='c_portfillo')

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کار ها'
    
    def __str__(self):
        return f'نمونه کار:{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=110, verbose_name='عنوان دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی  ها'
    
    def __str__(self):
        return f'دسته بندی ها:{self.title}'