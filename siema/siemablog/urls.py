from django.urls import path
# from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, ArticleListVew, ArticleDetailView, MaterialListVew, MaterialDetailView, ComicListVew, \
    ComicDetailView, QuizListVew, QuizDetailView

urlpatterns = [
                  # path('', views.home, name="home"),
                  path('', HomeView.as_view(), name="home"),
                  path('article/', ArticleListVew.as_view(), name='article-list'),
                  path('material/', MaterialListVew.as_view(), name='material-list'),
                  path('comic/', ComicListVew.as_view(), name='comic-list'),
                  path('quiz/', QuizListVew.as_view(), name='quiz-list'),
                  path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
                  path('material/<int:pk>', MaterialDetailView.as_view(), name='material-detail'),
                  path('comic/<int:pk>', ComicDetailView.as_view(), name='comic-detail'),
                  path('quiz/<int:pk>', QuizDetailView.as_view(), name='quiz-detail'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
