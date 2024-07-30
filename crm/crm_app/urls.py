from django.urls import path
from . import views as v

prefix_product = 'products/'
products = [
    path(prefix_product, v.ProductList.as_view(), name='products'),
    path(f'{prefix_product}new/', v.ProductCreate.as_view(), name='create_product'),
    path(f'{prefix_product}<int:product_id>', v.ProductDetail.as_view(), name='get_product'),
    path(f'{prefix_product}<int:product_id>/delete/', v.ProductDelete.as_view(), name='delete_product'),
    path(f'{prefix_product}<int:product_id>/edit/', v.ProductUpdate.as_view(), name='edit_product'),
]

prefix_ads = 'ads/'
ads = [
    path(prefix_ads, v.AdvertisementsList.as_view(), name='ads'),
    path(f'{prefix_ads}<int:ads_id>', v.AdvertisementsDetail.as_view(), name='get_ads'),
    path(f'{prefix_ads}<int:ads_id>/delete/', v.AdvertisementsDelete.as_view(), name='delete_ads'),
    path(f'{prefix_ads}<int:ads_id>/edit/', v.AdvertisementsUpdate.as_view(), name='edit_ads'),
    path(f'{prefix_ads}new/', v.AdvertisementsCreate.as_view(), name='create_ads'),
    path(f'{prefix_ads}statistic', v.AdvertisementsStatistic.as_view(), name='ads_statistic'),
]

prefix_leads = 'leads/'
leads = [
    path(prefix_leads, v.LeadList.as_view(), name='leads'),
    path(f'{prefix_leads}<int:lead_id>', v.LeadDetail.as_view(), name='get_lead'),
    path(f'{prefix_leads}<int:lead_id>/delete/', v.LeadDelete.as_view(), name='delete_lead'),
    path(f'{prefix_leads}<int:lead_id>/edit/', v.LeadUpdate.as_view(), name='edit_lead'),
    path(f'{prefix_leads}new/', v.LeadCreate.as_view(), name='create_lead'),
]

prefix_custom = 'customers/'
customers = [
    path(prefix_custom, v.CustomerList.as_view(), name='customers'),
    path(f'{prefix_custom}<int:customer_id>', v.CustomerDetail.as_view(), name='get_customer'),
    path(f'{prefix_custom}<int:customer_id>/delete/', v.CustomerDelete.as_view(), name='delete_customer'),
    path(f'{prefix_custom}<int:customer_id>/edit/', v.CustomerUpdate.as_view(), name='edit_customer'),
    path(f'{prefix_custom}new/', v.CustomerCreate.as_view(), name='create_customer'),
]

prefix_contract = 'contracts/'
contracts = [
    path(prefix_contract, v.ContractList.as_view(), name='contracts'),
    path(f'{prefix_contract}<int:contract_id>', v.ContractDetail.as_view(), name='get_contract'),
    path(f'{prefix_contract}<int:contract_id>/delete/', v.ContractDelete.as_view(), name='delete_contract'),
    path(f'{prefix_contract}<int:contract_id>/edit/', v.ContractUpdate.as_view(), name='edit_contract'),
    path(f'{prefix_contract}new/', v.ContractCreate.as_view(), name='create_contract'),
]

views = [
    path('', v.IndexView.as_view(), name='index'),
    path('login/', v.Login.as_view(), name='login'),
    path('accounts/logout/', v.Logout.as_view(), name='logout')
]

urlpatterns = views + customers + contracts + leads + ads + products
