from django.urls import path

from . import views
app_name = "polls"
urlpatterns = [
    path('',views.index, name = 'index'),
    path("<int:question_id>/", views.detail ,name = 'detail-page'),
    path("<int:question_id>/result/", views.results, name = "result-page"),
    path("<int:question_id>/vote/", views.vote, name="vote-page")
    
]