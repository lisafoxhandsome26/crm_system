from django.urls import path, re_path, register_converter
from . import views as v
from . import convertors as c

register_converter(c.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', v.index, name='home'),
    path('about/', v.about, name='about'),
    path('post/<int:post_id>/', v.show_post, name='post'),
    path('addpage/', v.add_page, name='add_page'),
    path('contact/', v.contact, name='contact'),
    path('login/', v.login, name='login'),
    path('category/<int:cat_id>/', v.show_category, name='category')
]
