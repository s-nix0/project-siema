# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Material, Comic, Quiz


# def home(request):
#     return render(request, 'home.html', {})


# class HomeView(ListView):
#     model = Post
#     template_name = 'home.html'


class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'latest_article'

    def get_queryset(self):
        return Post.objects.order_by('-pk')[:1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_material'] = Material.objects.order_by('-pk')[:1]
        context['comic_material'] = Comic.objects.order_by('-pk')[:1]
        context['quiz_material'] = Quiz.objects.order_by('-pk')[:1]
        return context


class ArticleListVew(ListView):
    model = Post
    template_name = 'test.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class MaterialListVew(ListView):
    model = Material
    template_name = 'test.html'


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'material_details.html'


class ComicListVew(ListView):
    model = Comic
    template_name = 'test.html'


class ComicDetailView(DetailView):
    model = Comic
    template_name = 'comic_details.html'


class QuizListVew(ListView):
    model = Quiz
    template_name = 'test.html'


class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quiz_details.html'
