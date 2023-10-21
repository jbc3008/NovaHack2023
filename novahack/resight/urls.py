from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("gafas/", views.obtener_gafas, name="obtener_gafas"),
    # ex: /polls/5/
    #path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    #path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    #path("<int:question_id>/vote/", views.vote, name="vote"),
    # Shit for the get API
    #path('gafas/', views.GafaList.as_view(), name='gafas-list'),

]