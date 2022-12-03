from django.db import models


class StarCategory(models.Model):
    category_id = models.CharField(max_length=10, verbose_name='ID')
    title = models.CharField(max_length=100, verbose_name='Название категории звезды')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категория звезд'
        verbose_name = 'Категория звезды'


class StarProfile(models.Model):
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=100, verbose_name='ФИО звезды')
    category = models.ForeignKey(StarCategory, on_delete=models.DO_NOTHING, related_name='star_profile')
    image = models.ImageField(upload_to='star-profile-image', verbose_name='Фото профиля')
    video = models.FileField(upload_to='star-video', verbose_name='Видео')
    banner = models.ImageField(upload_to='star-profile-banner', verbose_name='Баннер')
    description = models.TextField(verbose_name='О звезде', blank=True, null=True)
    deadline = models.IntegerField(verbose_name='Срок выполнения', default=3)
    price = models.CharField(max_length=50, verbose_name='Цена')
    popular = models.BooleanField(verbose_name='Категория популярные', default=False)
    star_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='ID популярные')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Звезды'
        verbose_name = 'Звезда'


class StarQuestionnaire(models.Model):
    star = models.ForeignKey(StarProfile, on_delete=models.CASCADE, related_name='questionnaire', verbose_name='Звезда')
    manager = models.CharField(max_length=100, verbose_name='Менеджер звезды')
    phone = models.CharField(max_length=50, verbose_name='Номер менеджера')
    price = models.CharField(max_length=50, verbose_name='Цена за выступление')
    location = models.CharField(max_length=200, verbose_name='Город')
    price_region = models.CharField(max_length=50, verbose_name='Цена за выступление')
    region = models.CharField(max_length=200, verbose_name='Регионы')


class Order(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=200, verbose_name='Телефон')
    star = models.CharField(max_length=200, verbose_name='Звезда')
    text = models.TextField(verbose_name='Текст', blank=True, null=True)

    def __str__(self):
        return self.name


class ManagerOrder(models.Model):
    user = models.CharField(max_length=100, verbose_name='Пользователь')
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=200, verbose_name='Телефон')
    star = models.CharField(max_length=100, verbose_name='Звезда')
    image = models.ImageField(upload_to='order_pay', verbose_name='Фото чека')
    text = models.TextField(verbose_name='Текст', blank=True, null=True)

    def __str__(self):
        return self.name


class StarVideo(models.Model):
    star = models.ForeignKey(StarProfile, on_delete=models.DO_NOTHING, related_name='star_video')
    image = models.ImageField(upload_to='star-video-image', verbose_name='Обложка видео')
    video = models.FileField(upload_to='star-order-video', verbose_name='Видео')
    banner = models.ImageField(upload_to='star-banner-image', verbose_name='Баннер')

    def __str__(self):
        return f'{self.id} {self.name}'


class StarReview(models.Model):
    text = models.TextField(verbose_name='Текст')
    profile = models.ForeignKey(StarProfile, on_delete=models.CASCADE, related_name='star_review',
                                verbose_name='Профиль')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile}\t {self.created}\n\t{self.text}"


class Banner(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название банера')
    image = models.ImageField(upload_to='banner-image', verbose_name='Фото')

    def __str__(self):
        return self.title


class About(models.Model):
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    email = models.CharField(max_length=50, verbose_name='Почта')
    whats_app = models.CharField(max_length=50, verbose_name='WhatsApp')
    telegram = models.CharField(max_length=50, verbose_name='Telegram')

    def __str__(self):
        return 'Контакты'


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=200, verbose_name='Телефон')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.name


class ToastsCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.title


class Toasts(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    category = models.ForeignKey(ToastsCategory, on_delete=models.DO_NOTHING, verbose_name='Категория')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

