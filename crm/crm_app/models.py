from django.db import models
from datetime import datetime


class Product:
    def __init__(self, pk, name, description, cost):
        self.pk = pk
        self.name = name
        self.description = description
        self.cost = cost


class Advertisement:
    def __init__(self, pk, name, leads_count, customers_count, profit):
        self.pk = pk
        self.name = name
        self.leads_count = leads_count
        self.customers_count = customers_count
        self.profit = profit


class Lead:
    def __init__(self, pk, last_name, first_name, email, phone):
        self.pk = pk
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.phone = phone


class Customer:
    def __init__(self, pk, lead: Lead):
        self.pk = pk
        self.lead = lead


class Contract:
    def __init__(self, pk, name, product: Product, start_date, end_date, cost):
        self.pk = pk
        self.name = name
        self.product = product
        self.start_date = start_date
        self.end_date = end_date
        self.cost = cost


def finder(object_id: int, list_objects: list):
    for col in list_objects:
        if col.pk == object_id:
            return col


viktor = Lead(1, "Бодрый", "Виктор", "fndffmf", 78463136)
victoria = Lead(2, "Диковина", "Виктория", "afmnfckmnfp", 4134946)
maria = Lead(3, "Битрубская", "Мария", "sndmfa;sdf", 1644894)
pr_1 = Product(1, "Программы под ключ", "Невероятные услуги предоставляемые здесь", 200)
pr_2 = Product(2, "Расчеты любой сложности", "Невероятные услуги предоставляемые здесь", 500)
cs_1 = Customer(1, victoria)
ca_2 = Customer(2, maria)
ad_1 = Advertisement(1, "Приходите к нам у нас лучшие программы", 20, 15, None)
ad_2 = Advertisement(2, "Расчеты с высочайшей точностью", 15, 23, 5)
con_1 = Contract(1, "№123", pr_1, "2024-07-12", "2024-12-31", 266)
con_2 = Contract(2, "№153", pr_1, "2024-07-12", "2024-11-20", 123)
list_pr = [pr_1, pr_2]
list_leads = [viktor, victoria, maria]
list_customers = [cs_1, ca_2]
list_ads = [ad_1, ad_2]
list_contracts = [con_1, con_2]