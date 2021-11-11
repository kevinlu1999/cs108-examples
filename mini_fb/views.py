from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse
from .models import Profile
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
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)
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
