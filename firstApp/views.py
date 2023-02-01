from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = "firstApp/index.html"

class NewsPageView(TemplateView):
    template_name = 'firstApp/news.html'

class CoursesPageView(TemplateView):
    template_name = "firstApp/courses_list.html"

class DocSitePageView(TemplateView):
    template_name = "firstApp/doc_site.html"

class LoginPageView(TemplateView):
    template_name = "firstApp/login.html"

class ContactsPageView(TemplateView):
    template_name = "firstApp/contacts.html"
