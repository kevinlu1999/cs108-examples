from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.views.generic.edit import DeleteView
from .models import Profile, StatusMessage
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm


# Create your views here.
class ShowAllProfilesView(ListView):
    model = Profile
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        return context


class CreateProfileView(CreateView):
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"


class UpdateProfileView(UpdateView):
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"
    queryset = Profile.objects.all()


def post_status_message(request, pk):
    if request.method == 'POST':
        form = CreateStatusMessageForm(
            request.POST or None, request.FILES or None)
        profile = Profile.objects.get(pk=pk)
        if form.is_valid():
            status_message = form.save(commit=False)
            image = form.save(commit=False)
            status_message.profile = profile
            image.profile = profile
            image.save()
            status_message.save()
        else:
            print("Error: the form was not valid")
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)


class DeleteStatusMessageView(DeleteView):
    template_name = "mini_fb/delete_status_form.html"
    queryset = StatusMessage.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DeleteStatusMessageView,
                        self).get_context_data(**kwargs)
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['st_msg'] = st_msg
        return context

    def get_object(self):
        return StatusMessage.objects.get(pk=self.kwargs['status_pk'])

    def get_success_url(self):
        profile_pk = self.kwargs['profile_pk']
        url = reverse('show_profile_page', kwargs={'pk': profile_pk})
        return url


class ShowNewsFeedView(DetailView):
    model = Profile
    template_name = "mini_fb/show_news_feed.html"
    context_object_name = "profile"


class ShowPossibleFriendsView(DetailView):
    model = Profile
    template_name = "mini_fb/show_possible_friends.html"
    context_object_name = "profile"


def add_friend(request, profile_pk, friend_pk):
        profile = Profile.objects.get(pk = profile_pk)
        friend = Profile.objects.get(pk = friend_pk)
        profile.friends.add(friend)
        profile.save()
        return redirect(reverse('show_profile_page', kwargs={'pk': profile_pk}))
