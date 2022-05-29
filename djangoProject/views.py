# from django.urls import reverse
# from django.http import HttpResponseRedirect
# from django.views.generic import TemplateView
#
# class AboutPage(TemplateView):
#     template_name = 'about.html'
#
# class LogoutPage(TemplateView):
#     template_name = 'logout.html'
#
# class HomePage(TemplateView):
#     template_name = "base.html"
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated():
#             return HttpResponseRedirect(reverse("test"))
#         return super().get(request, *args, **kwargs)
