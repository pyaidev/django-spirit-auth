from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, Group, Permission
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Country(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True, null=False)
    code = models.CharField(max_length=2, blank=False, unique=True, null=False)
    class Meta:
        app_label = 'userprofile'
        db_table = 'country'
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
    def __str__(self):
        return self.name
    
    



class City(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    class Meta:
        app_label = 'userprofile'
        db_table = 'city'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
    def __str__(self):
        return self.name
    
    
    
    




class SiteUser(AbstractUser):
    display_name = models.CharField(max_length=50, blank=False, unique=True, null=False)
    last_visit = models.DateTimeField(null=True)
    order_counts = models.IntegerField(default=0, null=True)  # количество покупок
    disput_counts = models.PositiveSmallIntegerField(default=0, null=True)  # количество диспутов
    win_disputs = models.PositiveSmallIntegerField(default=0, null=True)  # сколько раз выйграл диспуты
    note = models.TextField(max_length=300, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    # проверяем размер файла
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    user_avatar = models.ImageField(upload_to='images_avatar/%Y/%m/%d', blank=True, null=True,
                                    default='images_avatar/default.png')
    user_avatar_chat_thumbnail = ImageSpecField(source='user_avatar',
                                                processors=[ResizeToFill(120, 120)],
                                                format='JPEG',
                                                options={'quality': 60})
    user_avatar_thumbnail = ImageSpecField(source='user_avatar',
                                                processors=[ResizeToFill(42, 42)],
                                                format='JPEG',
                                                options={'quality': 60})
    block = models.BooleanField(default=False)
    blocked_by_id = models.IntegerField(null=True, blank=True)  # ID модератора, который заблокировал пользователя
    block_comment = models.CharField(max_length=250, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="siteuser_set",  # Change this related_name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="siteuser_set",  # Change this related_name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    class Meta:
        app_label = 'userprofile'
        db_table = 'userprofile'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
    USERNAME_FIELD = 'username'