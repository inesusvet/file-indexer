# ~*~ coding: utf-8 ~*~
from django.views.generic import (
    TemplateView,
    ListView,
)
from tagging.models import Tag
from tagging.views import tagged_object_list

from .models import *
from .forms import *

PAGE_SIZE = 50


class HomeView(TemplateView):
    """
    Главная страница с формой поиска
    """
    template_name = 'home.html'
    form_class = SearchForm

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['form'] = self.form_class()
        return context


class SearchResultsView(ListView):
    """
    Страница результатов поиска
    """
    context_object_name = 'video_list'
    paginate_by = PAGE_SIZE

    def validate_tag(self, query):
        """Попробуем найти тэг по переданному имени"""
        try:
            return Tag.objects.get(query)
        except Tag.DoesNotExist:
            return  # Не получилось

    def validate_video(self, qs, query):
        """Попробуем найти видео-файл по части имени"""
        qs = qs.filter(path__icontains=query)
        if qs.count():
            return qs

        return qs.none()  # Ничего не нашли

    def get_queryset(self):
        """Выберем из БД все подходящие видео-файлы"""
        qs = super(SearchResultsView, self).get_queryset()
        query = self.kwargs.get('query')

        tag = self.validate_tag(query)
        if tag:
            object_list = tagged_object_list(self.request, qs, tag)
            return object_list

        qs = self.validate_video(qs, query)
        return qs

    class Meta:
        model = Video
