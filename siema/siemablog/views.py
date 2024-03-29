from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, Material, Comic, Quiz, UserActivity
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SearchForm
from itertools import chain

# def home(request):
#     return render(request, 'home.html', {})


# class HomeView(ListView):
#     model = Post
#     template_name = 'home.html'


# @csrf_exempt  # Use CSRF exemption for simplicity. Ensure proper CSRF protection in production.
# @login_required(login_url='login')
# def update_user_activity(request):
#     if request.method == 'POST':
#         url = request.POST.get('url')
#         title = request.POST.get('title')
#         activity_type = request.POST.get('type')
#         level = request.POST.get('level')
#
#         # Assuming you have a UserActivity model instance for the current user
#         UserActivity.objects.create(
#             user=request.user,  # Assuming you are using Django authentication
#             activity_type=activity_type,
#             activity_level=level,  # Set the activity level
#         )
#
#         return JsonResponse({'status': 'success'})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
#
#     # Manually handle the case where the user is not authenticated
#     def auth_required(request):
#         return HttpResponseForbidden('Authentication required')


def handling_404(request, exception):
    return redirect('login')


class HomeView(TemplateView):
    template_name = 'home/index.html'


class AboutView(TemplateView):
    template_name = 'tentang/index.html'


class GuideView(TemplateView):
    template_name = 'panduan/index.html'


class SearchView(View):
    template_name = 'cari/index.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET)  # Bind the form to the GET data

        if form.is_valid():
            query = form.cleaned_data.get('query')

            # Perform a case-insensitive search on title and detail fields
            article_results = Post.objects.filter(Q(title__icontains=query) | Q(detail__icontains=query))
            material_results = Material.objects.filter(Q(title__icontains=query) | Q(detail__icontains=query))
            comic_results = Comic.objects.filter(Q(title__icontains=query) | Q(detail__icontains=query))
            quiz_results = Quiz.objects.filter(Q(title__icontains=query) | Q(detail__icontains=query))

            context = {
                'form': form,
                'query': query,
                'article_results': article_results,
                'material_results': material_results,
                'comic_results': comic_results,
                'quiz_results': quiz_results,
            }

            return render(request, self.template_name, context)

        # Handle the case when the form is not valid or no query provided
        return render(request, self.template_name, {'form': form, 'query': None})


# class DashboardView(LoginRequiredMixin, ListView):
#     template_name = 'dasbor/index.html'
#     context_object_name = 'dashboard_data'
#     model = User
#
#     def get_queryset(self):
#         # Return a queryset containing the current user
#         return User.objects.filter(pk=self.request.user.pk)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['latest_article'] = Post.objects.order_by('-pk')[:1]
#         context['latest_material'] = Material.objects.order_by('-pk')[:1]
#         context['latest_comic'] = Comic.objects.order_by('-pk')[:1]
#         context['latest_quiz'] = Quiz.objects.order_by('-pk')[:1]
#
#         # Get the latest user activity for the current user or provide a default value
#         try:
#             latest_user_activity = UserActivity.objects.filter(user=self.request.user).latest('last_activity')
#         except UserActivity.DoesNotExist:
#             latest_user_activity = None
#
#         context['latest_user_activity'] = latest_user_activity
#
#         return context


class DashboardView(LoginRequiredMixin, ListView):
    template_name = 'dasbor/index.html'
    # context_object_name = 'dashboard_data'
    model = User

    def get_queryset(self):
        # Return a queryset containing the current user
        return User.objects.filter(pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_article = Post.objects.order_by('-date_added')[:2]
        latest_material = Material.objects.order_by('-date_added')[:2]
        latest_comic = Comic.objects.order_by('-date_added')[:2]
        latest_quiz = Quiz.objects.order_by('-date_added')[:2]

        # Get the latest user activity for the current user or provide a default value
        try:
            latest_user_activity = UserActivity.objects.filter(
                user=self.request.user,
                activity_type__in=['Materi', 'Komik', 'Quiz']
            ).latest('last_activity')
        except UserActivity.DoesNotExist:
            latest_user_activity = None

        context['latest_user_activity'] = latest_user_activity

        # Combine data from different models into a single list
        all_latest_data = list(chain(latest_article, latest_material, latest_comic, latest_quiz))

        # Sort the list based on date_added in descending order
        all_latest_data.sort(key=lambda x: x.date_added, reverse=True)

        context['all_latest_data'] = all_latest_data
        return context


class ArticleListVew(ListView):
    model = Post
    template_name = 'test.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


def is_valid_level(model, level):
    # Implement your validation logic here
    # For example, check if the level exists in your database
    return model.objects.filter(level=level).exists()


class MaterialListVew(ListView):
    model = Material
    template_name = 'materi/index.html'
    context_object_name = 'material'


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'materi/list/materi_detail.html'

    def get_object(self, queryset=None):
        level = self.kwargs['level']

        # Check if the provided level is valid
        if not is_valid_level(self.model, level):
            # Redirect to the main directory
            return HttpResponseRedirect(reverse('material-list'))

        return get_object_or_404(Material, level=level)

    def get(self, request, *args, **kwargs):
        level = self.kwargs['level']
        queryset = Material.objects.all().order_by('level')
        self.object = self.get_object(queryset=queryset)

        if is_valid_level(self.model, level):
            # Log user activity
            UserActivity.objects.create(
                user=self.request.user,
                activity_title=self.object.title,
                activity_type=self.object.type,
                activity_level=self.object.level
            )

            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)

        else:
            return HttpResponseRedirect(reverse('material-list'))


class ComicListVew(ListView):
    model = Comic
    template_name = 'komik/index.html'
    context_object_name = 'comic'


class ComicDetailView(DetailView):
    model = Comic
    template_name = 'komik/list/komik_detail.html'

    def get_object(self, queryset=None):
        level = self.kwargs['level']

        # Check if the provided level is valid
        if not is_valid_level(self.model, level):
            # Redirect to the main directory
            return HttpResponseRedirect(reverse('comic-list'))

        return get_object_or_404(Comic, level=level)

    def get(self, request, *args, **kwargs):
        level = self.kwargs['level']
        queryset = Comic.objects.all().order_by('level')
        self.object = self.get_object(queryset=queryset)

        if is_valid_level(self.model, level):
            # Log user activity
            UserActivity.objects.create(
                user=self.request.user,
                activity_title=self.object.title,
                activity_type=self.object.type,
                activity_level=self.object.level
            )

            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)

        else:
            return HttpResponseRedirect(reverse('comic-list'))


class QuizListVew(ListView):
    model = Quiz
    template_name = 'kuis/index.html'
    context_object_name = 'quiz'


class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'kuis/list/kuis_detail.html'

    def get_object(self, queryset=None):
        level = self.kwargs['level']

        # Check if the provided level is valid
        if not is_valid_level(self.model, level):
            # Redirect to the main directory
            return HttpResponseRedirect(reverse('quiz-list'))

        return get_object_or_404(Quiz, level=level)

    def get(self, request, *args, **kwargs):
        level = self.kwargs['level']
        queryset = Quiz.objects.all().order_by('level')
        self.object = self.get_object(queryset=queryset)

        if is_valid_level(self.model, level):
            # Log user activity
            UserActivity.objects.create(
                user=self.request.user,
                activity_title=self.object.title,
                activity_type=self.object.type,
                activity_level=self.object.level
            )

            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)

        else:
            return HttpResponseRedirect(reverse('quiz-list'))


class ToS(TemplateView):
    template_name = 'tos/index.html'


class PrivacyPolicy(TemplateView):
    template_name = 'privacy_policy/index.html'
