from django.views import generic
from django.http import HttpResponseRedirect

from forms import ProfileForm
from models import UserProfile


class Home(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated():
            profile = UserProfile.objects.get_or_create(user=self.request.user)[0]
            context['form'] = ProfileForm(instance=profile)
        context['request'] = self.request
        return context

    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/')
        profile = UserProfile.objects.get_or_create(user=request.user)[0]
        form = ProfileForm(self.request.POST, instance=profile)
        if form.is_valid():
            form.save()
            context = {'msg': 'Thank you for your support!',
                       'request': request}
            return self.render_to_response(context)
        else:
            context = self.get_context_data(request)
            context['form'] = form
            return self.render_to_response(context)


