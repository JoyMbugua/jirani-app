from django.shortcuts import render, redirect
from .forms import ContactCreateForm, BusinessForm
from .models import Contact, Business
from django.urls import reverse

def add_contact(request):
    form = ContactCreateForm()
    if request.method == 'POST':
        form = ContactCreateForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=True)
            contact.save()
            return redirect('contacts_list')
    return render(request, 'location/create_contact.html', {"form": form})

def ContactViewList(request):
    contacts = Contact.objects.all().order_by('-pk')

    new_contacts = []
    for contact in contacts:
        if contact.get_location() == request.user.get_location():
            new_contacts.append(contact)
    return render(request, 'location/contactlist.html', {"contacts": new_contacts})

def add_business(request):
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.owner = request.user
            biz.save()
            return redirect('business_list')
    return render(request, 'location/add_business.html', {"form": form})

def neighborhood_details(request):
    user = request.user
    area = user.get_location()
    occupants = area.get_count()
    biz_count = area.count_businesses()
    context = {"occupants": occupants, "area": area, "biz_count": biz_count}
    return render(request, 'location/about.html', context)

def search_business(request):
    searched_word = request.GET.get('searchword')
    business_list = Business.search_business(searched_word)
    return render(request, 'location/search.html', {"business_list": business_list, "searched_word": searched_word})




