from django.views.generic import TemplateView

# Create your views here.

class ShowHelloWorld(TemplateView):
    template_name='hello_world.html'

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
