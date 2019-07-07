from django.views.generic.base import TemplateView

"""
https://docs.djangoproject.com/en/dev/ref/class-based-views/base/#templateview
"""

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
