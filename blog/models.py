from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

NULLABLE = {"blank": True, "null": True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Названиие блога')
    slug = models.CharField(max_length=255, unique=True, **NULLABLE)
    content = models.TextField(verbose_name="Содержимое блога")
    preview = models.ImageField(upload_to='media/photo', **NULLABLE)
    created_date = models.DateTimeField(auto_created=True, default=timezone.now)
    is_published = models.BooleanField(default=True, verbose_name='опубликован')
    views_count = models.IntegerField(verbose_name='Просмотры', default=0)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title", "content"]

    def __str__(self):
        return self.title
