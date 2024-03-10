import typing as ty

from django import template
from django.urls import ResolverMatch

from ..models import PostCategoryChoices

register = template.Library()


@register.simple_tag
def get_categories() -> ty.List[ty.Dict[str, str]]:
    """Формируем удобный список категории для менюшки"""

    result: ty.List[ty.Dict[str, str]] = list()
    for category, label in dict(PostCategoryChoices.choices).items():
        result.append({"category": category, "label": label})

    return result


@register.filter
def is_active(resolver_match: ResolverMatch, path_name: str) -> str:
    """Првоеряем, какая категория сейчас активная"""

    style: str = "border: 2px solid rgb(61, 146, 201)"
    if resolver_match.url_name == path_name:
        return style

    if resolver_match.kwargs.get("name") == path_name:
        return style
