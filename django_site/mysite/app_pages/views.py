from django.views.generic import TemplateView

from app_pages.apps import AppPagesConfig

app_name = AppPagesConfig.name


class Page1View(TemplateView):
    name = '1.html'
    view_name = 'page_1'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page11View(TemplateView):
    name = '1.1.html'
    view_name = 'page_1_1'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page12View(TemplateView):
    name = '1.2.html'
    view_name = 'page_1_2'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page121View(TemplateView):
    name = '1.2.1.html'
    view_name = 'page_1_2_1'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page122View(TemplateView):
    name = '1.2.2.html'
    view_name = 'page_1_2_2'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page13View(TemplateView):
    name = '1.3.html'
    view_name = 'page_1_3'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page14View(TemplateView):
    name = '1.4.html'
    view_name = 'page_1_4'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page2View(TemplateView):
    name = '2.html'
    view_name = 'page_2'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page21View(TemplateView):
    name = '2.1.html'
    view_name = 'page_2_1'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page211View(TemplateView):
    name = '2.1.1.html'
    view_name = 'page_2_1_1'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page212View(TemplateView):
    name = '2.1.2.html'
    view_name = 'page_2_1_2'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page2121View(TemplateView):
    name = '2.1.2.1.html'
    view_name = 'page_2_1_2_1'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page2122View(TemplateView):
    name = '2.1.2.2.html'
    view_name = 'page_2_1_2_2'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page22View(TemplateView):
    name = '2.2.html'
    view_name = 'page_2_2'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page3View(TemplateView):
    name = '3.html'
    view_name = 'page_3'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page31View(TemplateView):
    name = '3.1.html'
    view_name = 'page_3_1'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page4View(TemplateView):
    name = '4.html'
    view_name = 'page_4'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page41View(TemplateView):
    name = '4.1.html'
    view_name = 'page_4_1'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page411View(TemplateView):
    name = '4.1.1.html'
    view_name = 'page_4_1_1'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page412View(TemplateView):
    name = '4.1.2.html'
    view_name = 'page_4_1_2'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}


class Page413View(TemplateView):
    name = '4.1.3.html'
    view_name = 'page_4_1_3'
    template_name = f'{app_name}/{name}'
    extra_context = {'url_name': f'{app_name}:{view_name}'}
