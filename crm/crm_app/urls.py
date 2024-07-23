from django.urls import path
from . import views as v


prefix_product = 'products/'
products = [
    path(prefix_product, v.products_list, name='products'),
    path(f'{prefix_product}new', v.create_product, name='create_product'),
    path(f'{prefix_product}<int:product_id>', v.get_product, name='create_product'),
    path(f'{prefix_product}<int:product_id>/delete', v.delete_product, name='delete_product'),
    path(f'{prefix_product}<int:product_id>/edit', v.edit_product, name='edit_product'),
]

prefix_ads = 'ads/'
ads = [
    path(prefix_ads, v.advertisements_list, name='ads'),
    path(f'{prefix_ads}<int:ads_id>', v.get_advertisements, name='get_ads'),
    path(f'{prefix_ads}<int:ads_id>/delete', v.delete_advertisements, name='delete_ads'),
    path(f'{prefix_ads}<int:ads_id>/edit/', v.edit_advertisements, name='edit_ads'),
    path(f'{prefix_ads}new', v.create_advertisements, name='create_ads'),
    path(f'{prefix_ads}statistic', v.get_ads_statistic, name='ads_statistic'),
]

prefix_leads = 'leads/'
leads = [
    path(prefix_leads, v.leads_list, name='leads'),
    path(f'{prefix_leads}<int:lead_id>', v.get_lead, name='get_lead'),
    path(f'{prefix_leads}<int:lead_id>/delete', v.delete_lead, name='delete_lead'),
    path(f'{prefix_leads}<int:lead_id>/edit/', v.edit_lead, name='edit_lead'),
    path(f'{prefix_leads}new', v.create_lead, name='create_lead'),
]

prefix_custom = 'customers/'
customers = [
    path(prefix_custom, v.customers_list, name='customers'),
    path(f'{prefix_custom}<int:customer_id>', v.get_customer, name='get_customer'),
    path(f'{prefix_custom}<int:customer_id>/delete', v.delete_customer, name='delete_customer'),
    path(f'{prefix_custom}<int:customer_id>/edit/', v.edit_customer, name='edit_customer'),
    path(f'{prefix_custom}new', v.create_customer, name='create_customer'),
]

prefix_contract = 'contracts/'
contracts = [
    path(prefix_contract, v.contracts_list, name='contracts'),
    path(f'{prefix_contract}<int:contract_id>', v.get_contract, name='get_contract'),
    path(f'{prefix_contract}<int:contract_id>/delete', v.delete_contract, name='delete_contract'),
    path(f'{prefix_contract}<int:contract_id>/edit/', v.edit_contract, name='edit_contract'),
    path(f'{prefix_contract}new', v.create_contract, name='create_contract'),
]

views = [
    path('', v.index, name='index'),
]

urlpatterns = views + customers + contracts + leads + ads + products
