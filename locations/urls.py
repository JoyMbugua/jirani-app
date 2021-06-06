from django.urls import path
from .views import add_contact, ContactViewList, add_business, neighborhood_details, search_business, create_neighborhood, BusinessListView

urlpatterns = [ 
    path('add_contact/', add_contact, name='add_contact'),
    path('contacts/', ContactViewList, name='contacts_list'),
    path('add_business/', add_business, name='add_business'),
    path('about/', neighborhood_details, name='about_neighborhood'),
    path('search/', search_business, name='search_business'),
    path('add_neighborhood/', create_neighborhood, name='add_neighborhood'),
    path('businesses/', BusinessListView, name='business_list')
]