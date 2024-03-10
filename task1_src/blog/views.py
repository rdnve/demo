import typing as ty

from django import __version__ as django_version
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import FeedbackForm, YearForm
from .indexes import DATA_ABOUT
from .models import Post, PostCategoryChoices, PostQuerySet
from .utils import plural


def root(request: HttpRequest) -> HttpResponse:
    """Главная страница"""

    qs: PostQuerySet[Post] = Post.objects.all()

    template_name: str = "root.html"
    context: ty.Dict[str, str] = {"title": "Главная страница", "posts": qs}

    return render(request=request, template_name=template_name, context=context)


def about(request: HttpRequest) -> HttpResponse:
    """Страница об авторе"""

    template_name: str = "about.html"
    context: ty.Dict[str, ty.Any] = {
        "title": "О нас",
        "data": DATA_ABOUT,
    }

    return render(request=request, template_name=template_name, context=context)


def technology(request: HttpRequest) -> HttpResponse:
    """Страница об авторе"""

    template_name: str = "technology.html"
    context: ty.Dict[str, ty.Any] = {
        "title": "О технологиях",
        "django_version": django_version,
    }

    return render(request=request, template_name=template_name, context=context)


def feedback(request: HttpRequest) -> HttpResponse:
    """Страница написать автору"""

    is_saved: bool = False
    if request.method == "POST":
        form = FeedbackForm(data=request.POST)
        if not form.is_valid():
            raise Http404("Форма некорректная.")

        is_saved = bool(form.save())

    template_name: str = "feedback.html"
    context: ty.Dict[str, ty.Any] = {
        "title": "Обратная связь",
        "is_saved": is_saved,
        "form": FeedbackForm(),
    }

    return render(request=request, template_name=template_name, context=context)


def category(request: HttpRequest, name: str) -> HttpResponse:
    """Записи конкретной категории"""

    if name not in PostCategoryChoices.values:
        raise Http404(f"Такой категории «{name}» нет.")

    qs: PostQuerySet[Post] = Post.objects.filter(category=name)
    if not qs.exists():
        raise Http404(
            f"Извините, но записей в категории "
            f"«{PostCategoryChoices[name.upper()].label}» нет."
        )

    # отдельно каунт, чтоб ниже дважды не вызывать его
    count: int = qs.count()
    template_name: str = "category.html"
    context: ty.Dict[str, ty.Any] = {
        "title": PostCategoryChoices[name.upper()].label,
        "subtitle": "Всего в категории {count} {plural}".format(
            count=count,
            plural=plural(count, ["запись", "записи", "записей"]),
        ),
        "count": qs.count(),
        "posts": qs,
    }

    return render(request=request, template_name=template_name, context=context)


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    """Записи конкретной категории"""

    try:
        post: Post = Post.objects.get_by_slug(value=slug)
    except Post.DoesNotExist as e:
        raise Http404("По такой ссылке запись не найдена.")

    template_name: str = "post_detail.html"
    context: ty.Dict[str, ty.Any] = {
        "title": "О нас",
        "post": post,
    }

    return render(request=request, template_name=template_name, context=context)


def year(request: HttpRequest) -> HttpResponse:
    """Записи конкретной категории"""

    year, is_leap = None, None
    if request.method == "POST":
        form = YearForm(data=request.POST)
        if not form.is_valid():
            raise Http404("Форма некорректная.")

        year = form.cleaned_data["year"]

        is_leap = False
        # разделенный на 100 означает столетний год (оканчивающийся на 00),
        # столетний год, разделенный на 400, является високосным годом
        if (year % 400 == 0) and (year % 100 == 0):
            is_leap = True

        # не разделенное на 100 означает не столетний год
        # год разделить на 4 — високосный год
        elif (year % 4 == 0) and (year % 100 != 0):
            is_leap = True

    template_name: str = "year.html"
    context: ty.Dict[str, ty.Any] = {
        "title": "Определение года",
        "form": YearForm(),
        "is_leap": is_leap,
        "year": year,
        "century": (year // 100) + 1 if year else None,
    }

    return render(request=request, template_name=template_name, context=context)
