from django.views.generic import TemplateView


class ManagementView(TemplateView):
    template_name = 'management/base.html'

    def get_context_data(self, **kwargs):
        context = super(ManagementView, self).get_context_data(**kwargs)
        if self.request.user.is_staff:
            context['profile'] = {'nav': 'profile', 'url': '/security/profile'}
        return context