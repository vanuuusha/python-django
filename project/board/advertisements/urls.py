from django.urls import path
from . import views


urlpatterns = [
    path("", views.AdvertisementsList.as_view(), name='advertisements_list'),
    path("advertisement/", views.advertisement_deatails, name='advertisement_deatails'),
    path("python-basic/",  views.python_basic, name='python_basic'),
    path("django/", views.django, name='django'),
    path("frontend-developer/", views.frontend_developer, name='frontend_developer'),
    path("layout-basic/", views.layout_basic, name="layout_basic"),
    path("java/", views.java, name="java"),
    path("contacts/", views.contacts, name="contacts"),
    path("about-us/", views.about_us, name="about_us"),
    path("categories/", views.categories_page, name="categories"),
    path("regions/", views.RegionsPage.as_view(), name="regions")
]
