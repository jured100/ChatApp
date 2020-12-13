from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import ModelFormMixin, UpdateView
from rest_framework.generics import ListAPIView, CreateAPIView

from .forms import SubmissionForm, ProfileForm
from .models import Message
# Create your views here.
# Registracija, login (logout je pod template)
from .serializers import MessageSerializer


def home_view(request, *args):
    return render(request, "about.html")


def register_view(request):
    # if request.user.is_authenticated:
    # return redirect('djangobin:profile', username=request.user.username)

    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect("/")

    else:
        f = UserCreationForm()

    return render(request, 'register.html', {'form': f})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

    return render(request, "login.html")


def logout_view(request):
    return logout(request)


class ChatView(ModelFormMixin, ListView):
    template_name = 'groupchat.html'
    model = Message
    form_class = SubmissionForm

    def get_queryset(self):
        qs = Message.objects.filter(receiver__isnull=True)
        other_user = self.kwargs.get('other_user')

        if other_user:
            qs = Message.objects.filter(receiver=other_user)

        return qs


def group_chat_view(request, *context, **kwargs):
    qs = Message.objects.filter(receiver__isnull=True)
    other_user = None
    other_user_id = kwargs.get('receiving_user__id')
    form = SubmissionForm(request.POST)
    print(other_user_id)
    context = {}

    if other_user_id:
        other_user = get_object_or_404(get_user_model(), pk=other_user_id)
        qs = Message.objects.filter(
            Q(receiver=other_user, sender=request.user) | Q(receiver=request.user, sender=other_user)
        )
        context['other_user_id'] = other_user_id

    if request.method == 'POST':
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            if other_user:
                message.receiver = other_user
            message.save()
            form = SubmissionForm()
            return HttpResponseRedirect(request.path_info)

    context['form'] = form
    context['qs'] = qs
    context['kwargs'] = kwargs
    return render(request, "groupchat.html", context)


def users_view(request):
    Users = get_user_model()
    users = Users.objects.all()
    args = {"users": users}
    return render(request, "users.html", args)


class UserMessageView(TemplateView):
    template_name = 'groupchat.html'


def user_view(request):
    userId = request.kw
    data = User.objects.get(id=userId)
    # comm = Komentarji.objects.all().filter(recept_id=recipeId)
    # info = ReceptiSestavine.objects.all().filter(recept_id=recipeId)
    # face = Postopki.objects.all().filter(recept_id=recipeId)
    # rate = Ocene.objects.all().filter(recept_id=recipeId)

    # args = {"data": data, "comm": comm, "face": face, "info": info,"rate": rate}
    # return render(request, "dodajrecept.html", args)

    # return render(request, "recept.html", args)

    return render(request, "user.html", data)


class ProfileView(UpdateView):
    template_name = "profile.html"
    model = get_user_model()
    form_class = ProfileForm

    def get_success_url(self):
        return reverse('message:profile', kwargs={'pk': self.kwargs['pk']})


def profile_view(request):
    return render(request, "profile.html")


class MessageListView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        qs = Message.objects.filter(receiver__isnull=True)
        u = self.request.user

        if pk:
            other_user = get_object_or_404(get_user_model(), pk=pk)
            qs = Message.objects.filter(
                Q(receiver=other_user, sender=u) | Q(receiver=u, sender=other_user)
            )

        return qs


class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

