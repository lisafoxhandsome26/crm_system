from django.shortcuts import render
from django.http import Http404
from ..models import finder, list_contracts


def contracts_list(request):
    data = {"contracts": list_contracts}
    return render(request, "contracts/contracts-list.html", context=data)


def get_contract(request, contract_id: int):
    contract = finder(contract_id, list_contracts)
    if contract:
        data = {"object": contract}
        return render(request, "contracts/contracts-detail.html", context=data)
    else:
        raise Http404()


def delete_contract(request, contract_id: int):
    contract = finder(contract_id, list_contracts)
    if contract:
        data = {"object": contract}
        return render(request, "contracts/contracts-delete.html", context=data)
    else:
        raise Http404()


def edit_contract(request, contract_id: int):
    contract = finder(contract_id, list_contracts)
    if contract:
        data = {"object": contract}
        return render(request, "contracts/contracts-edit.html", context=data)
    else:
        raise Http404()


def create_contract(request):
    return render(request, "contracts/contracts-create.html")
