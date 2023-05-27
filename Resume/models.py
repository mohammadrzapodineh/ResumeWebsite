from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length=110,verbose_name='عنوان مهارت')
    persent= models.IntegerField(default=0, verbose_name='درصد تسلط')


    class Meta:
        ordering = ['-persent']
        verbose_name = 'مهارت '
        verbose_name_plural = 'مهارت ها'

    def __str__(self):
        return self.title 


class Biography(models.Model):
    name = models.CharField(max_length=110, verbose_name='نام ')
    lived_in = models.CharField(max_length=50, verbose_name='محل زندگی ')
    avatar = models.ImageField(verbose_name='اواتار', upload_to='biography/avatar/', blank=True, null=True)
    biography = models.TextField(verbose_name='بیوگرافی در مورد خود')
    total_projects = models.IntegerField(default=0, verbose_name='پروژه های موفق')
    experince = models.IntegerField(verbose_name='تجربه کار بر اساس سال', default=0)

    
    class Meta:
        verbose_name = 'بیوگرافی'
        verbose_name_plural = 'بیوگرافی ها'

    def __str__(self):
        return f'بیوگرافی: {self.name}-'


class Service(models.Model):
    title = models.CharField(max_length=110, verbose_name='عنوان خدمات')
    description = models.TextField(verbose_name='توضیحات خدمات')
    service_icon = (
        ('fas fa-cogs', 'آیکون چرخ دنده'),
        ('fas fa-desktop', 'آیکون دسکتاپ'),
        ('fas fa-mobile-alt', 'آیکون موبایل'),
        ('fas fa-medkit', 'آیکون جعبه کمک اولیه')
    )
    icon = models.CharField(choices=service_icon, max_length=30, verbose_name='آیکون برای خدمت مورد نظر')


    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'


    def __str__(self):
        return f'آیکون:{self.title}'


class Favorite(models.Model):
    title = models.CharField(max_length=110, verbose_name='عنوان علاقه مندی شما')
    favoraite_icon = (
        ('fas fa-music', 'آیکون موزیک'),
        ('fas fa-route', 'آیکون گردشگری'),
        ('fas fa-image', 'آیکون تصاویر'),
        ('fas fa-film', 'آیکون فیلم'),
        ('fas fa-space-shuttle', 'آیکون سفینه فضایی'),
        ('fas fa-book', 'آیکون کتاب'),
        ('fas fa-gamepad', 'آیکون بازی'),
        ('fas fa-tree', 'آیکون درخت')
    )
    icon = models.CharField(choices=favoraite_icon, max_length=40, verbose_name='آیکون')


    class Meta:
        verbose_name = 'علاقه'
        verbose_name_plural = 'علایق'


    def __str__(self):
        return f'آیکون:{self.title}'


class WorkExperince(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان سابقه کاری')
    date_joined = models.DateField(verbose_name='تاریخ شروع کار')
    date_left = models.DateField(blank=True, null=True, verbose_name='تاریخ پایان کار')
    company = models.CharField(max_length=110, verbose_name='شرکت محل کار')
    description = models.TextField(verbose_name='توضیحات سابقه کاری', blank=True, null=True)

    class Meta:
        verbose_name = 'سابقه کاری'
        verbose_name_plural = 'سوابق کاری'


    def __str__(self):
        return f'سابقه کاری  :{self.title}- {self.company}'


class Educational(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان سابقه تحصیلی')
    date_joined = models.DateField(verbose_name='تاریخ شروع ')
    date_left = models.DateField(blank=True, null=True, verbose_name='تاریخ پایان')
    college = models.CharField(max_length=110, verbose_name='نام کالج')
    description = models.TextField(verbose_name='توضیحات سابقه تحصیلی', blank=True, null=True)


    class Meta:
        verbose_name = 'سابقه تحصیلی'
        verbose_name_plural = 'سوابق تحصیلی'


    def __str__(self):
        return f'سابقه تحصیلی  :{self.title}- {self.college}'



class SocialMedia(models.Model):
    name = models.CharField(max_length=110, verbose_name=' نام شبکه اجتماعی')
    link = models.URLField(verbose_name='لینک شبکه اجتماعی شما')
    social_icon = (
        ('fab fa-facebook-f', 'آیکون فیسبوک'),
        ('fab fa-twitter', 'آیکون توییتر'),
        ('fab fa-instagram', 'آیکون اینستاگرم'),
        ('fab fa-youtube', 'آیکون یوتیوب'),

    )
    icon = models.CharField(choices=social_icon, max_length=40, verbose_name='آیکون')


    class Meta:
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'


    def __str__(self):
        return f'آیکون:{self.name}'
