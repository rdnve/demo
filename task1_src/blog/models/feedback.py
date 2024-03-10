from __future__ import annotations

from django.db import models
from django.utils import timezone as tz


class Feedback(models.Model):
    """Модель обратной связи"""

    full_name: str = models.CharField(
        "полное имя",
        max_length=128,
    )
    email: str = models.EmailField(
        "почта",
        max_length=128,
    )
    message: str = models.TextField("сообщение")
    created_at: tz.datetime = models.DateTimeField(
        "время отправки",
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"

    def __str__(self) -> str:
        return f"{self.full_name}: {self.email}"
