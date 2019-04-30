from django.urls import re_path

from experiments import views


urlpatterns = [
    re_path(r'^goal/(?P<goal_name>[^/]+)/(?P<cache_buster>[^/]+)?$', views.record_experiment_goal, name="experiment_goal"),
    re_path(r'^confirm_human/$', views.confirm_human, name="experiment_confirm_human"),
    re_path(r'^change_alternative/(?P<experiment_name>[a-zA-Z0-9-_]+)/(?P<alternative_name>[a-zA-Z0-9-_]+)/$', views.change_alternative, name="experiment_change_alternative"),
]
