from __future__ import annotations

import typing as ty

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone as tz
from django.utils.text import Truncator
from slugify import slugify

User = get_user_model()


class PostCategoryChoices(models.TextChoices):
    """Категория записи"""

    SCIENCE = "science", "Наука"
    MUSIC = "music", "Музыка"
    CINEMA = "cinema", "Кинематограф"
    OTHER = "other", "Другое"


class PostQuerySet(models.QuerySet):
    """Запросы к таблице"""

    def get_by_slug(self, value: str) -> Post:
        """Вернуть запись по красивом урлу"""

        try:
            pk = int(value.split("-")[0])
        except (IndexError, TypeError, ValueError):
            raise Post.DoesNotExist("Запись с таким идентификатором не найдена.")
        else:
            return self.get(pk=pk)


class PostManager(models.Manager.from_queryset(PostQuerySet)):
    """Менеджер управления запросами к базе"""


class Post(models.Model):
    """Модель поста (новости)"""

    title: str = models.CharField(
        "заголовок",
        max_length=128,
        blank=False,
        null=False,
    )
    subtitle: ty.Optional[str] = models.CharField(
        "подзаголовок",
        max_length=128,
        blank=True,
        null=True,
    )
    body: str = models.TextField("тело поста")
    created_at: tz.datetime = models.DateTimeField(
        "время добавления",
        auto_now_add=True,
        editable=False,
    )
    created_by: User = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", verbose_name="автор"
    )
    category: str = models.CharField(
        verbose_name="категория",
        choices=PostCategoryChoices.choices,
        default=PostCategoryChoices.OTHER,
        max_length=128,
    )
    picture = models.ImageField("изображение", upload_to="pictures/", blank=True)

    objects = PostManager()

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "запись"
        verbose_name_plural = "записи"

    def __str__(self) -> str:
        return self.title

    @property
    def slugify(self) -> str:
        """Сформировать красивую ссылку"""

        return f"{self.id}-{" - ".join(slugify(self.title).split(" - ")[:3])}"

    @property
    def description(self) -> str:
        """Обрезанная версия"""

        return Truncator(self.body).words(25)

    @property
    def category_style(self) -> str:
        """Вернуть правильный CSS-селектор"""

        styles: ty.List[str] = ["design", "pure", "yui", "js"]
        return (
            "post-category-" + styles[PostCategoryChoices.values.index(self.category)]
        )

    @property
    def url(self) -> str:
        """Сформировать ссылку до записи"""

        return reverse("blog:post_detail", args=[self.slugify])

    @property
    def category_url(self) -> str:
        """Сформировать ссылку до категории"""

        return reverse("blog:category", args=[self.category])
