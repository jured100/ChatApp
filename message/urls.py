from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import home_view, register_view, login_view, group_chat_view, users_view, ProfileView, MessageListView, \
    MessageUpdateView

# ViewSets define the view behavior.


app_name = 'message'

urlpatterns = [
    path("", home_view, name="home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("groupchat/", group_chat_view, name="groupchat"),
    # path("/", logout_view, name="logout"),
    path("logout", auth_views.LogoutView.as_view(next_page='/'), name="logout"),
    path('users/', users_view, name="users"),
    path('profile/<int:pk>', ProfileView.as_view(), name="profile"),
    path('private_message/<int:receiving_user__id>', group_chat_view, name="private_message"),
    path('list/', MessageListView.as_view(), name='list'),
    path('update/', csrf_exempt(MessageUpdateView.as_view()), name='update'),
]
