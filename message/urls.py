from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import home_view, register_view, login_view, group_chat_view, users_view, ProfileView, MessageListView, \
    MessageCreateView

# ViewSets define the view behavior.


app_name = 'message'

urlpatterns = [
    path("", home_view, name="home"),

    path("login/", login_view, name="login"),
    path("logout", auth_views.LogoutView.as_view(next_page='/'), name="logout"),

    path("register/", register_view, name="register"),
    path('users/', users_view, name="users"),

    # Classic calls
    path('profile/<int:pk>', ProfileView.as_view(), name="profile"),

    path('groupchat/', group_chat_view, name="groupchat"),
    path('private_message/<int:receiving_user__id>', group_chat_view, name="private_message"),

    # REST calls
    path('list/', MessageListView.as_view(), name='list'),
    path('list/<int:pk>', MessageListView.as_view(), name='list_private'),
    path('create/', csrf_exempt(MessageCreateView.as_view()), name='create'),
    path('create/<int:pk>', csrf_exempt(MessageCreateView.as_view()), name='create_private'),
]



