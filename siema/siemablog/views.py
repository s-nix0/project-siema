# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Material, Comic, Quiz, UserActivity
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

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


class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'latest_article'

    def get_queryset(self):
        return Post.objects.order_by('-pk')[:1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_material'] = Material.objects.order_by('-pk')[:1]
        context['latest_comic'] = Comic.objects.order_by('-pk')[:1]
        context['latest_quiz'] = Quiz.objects.order_by('-pk')[:1]

        # Try to get the latest user activity or provide a default value
        try:
            latest_user_activity = UserActivity.objects.latest('last_activity')
        except UserActivity.DoesNotExist:
            latest_user_activity = None

        context['latest_user_activity'] = latest_user_activity

        return context


class ArtikelListVew(ListView):
    model = Post
    template_name = 'test.html'


class ArtikelDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class MateriListVew(ListView):
    model = Material
    template_name = 'test.html'


class MateriDetailView(DetailView):
    model = Material
    template_name = 'test.html'

    def get_object(self, queryset=None):
        level = self.kwargs['level']
        return get_object_or_404(Material, level=level)

    def get(self, request, *args, **kwargs):
        # Get the quiz object
        self.object = self.get_object()

        # Log user activity
        UserActivity.objects.create(
            user=self.request.user,
            activity_title=self.object.title,
            activity_type=self.object.type,
            activity_level=self.object.level
        )

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class KomikListVew(ListView):
    model = Comic
    template_name = 'test.html'


class KomikDetailView(DetailView):
    model = Comic
    template_name = 'comic_details.html'

    def get_object(self, queryset=None):
        level = self.kwargs['level']
        return get_object_or_404(Comic, level=level)

    def get(self, request, *args, **kwargs):
        # Get the quiz object
        self.object = self.get_object()

        # Log user activity
        UserActivity.objects.create(
            user=self.request.user,
            activity_title=self.object.title,
            activity_type=self.object.type,
            activity_level=self.object.level
        )

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class KuisListVew(ListView):
    model = Quiz
    template_name = 'test.html'


class KuisDetailView(DetailView):
    model = Quiz
    template_name = 'test.html'

    def get_object(self, queryset=None):
        level = self.kwargs['level']
        return get_object_or_404(Quiz, level=level)

    def get(self, request, *args, **kwargs):
        # Get the quiz object
        self.object = self.get_object()

        # Log user activity
        UserActivity.objects.create(
            user=self.request.user,
            activity_title=self.object.title,
            activity_type=self.object.type,
            activity_level=self.object.level
        )

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
