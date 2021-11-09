from django.urls import path
from .views import ShowAllProfilesView, ShowProfilePageView, CreateProfileView, UpdateProfileView, post_status_message


urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('create_profile', CreateProfileView.as_view(), name="create_profile"),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
    path('profile/<int:pk>/post_status', post_status_message, name="post_status"),
]
