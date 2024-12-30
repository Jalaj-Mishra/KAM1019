from django.shortcuts import render
from .models import Lead
from .forms import LeadForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, 'index.html')



def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'lead_list.html', {'leads': leads})


@login_required
def add_lead(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            newLead = form.save(commit = False)
            newLead.save()
            return redirect('lead_list')
    else:
        form = LeadForm()
    return render(request, 'lead_form.html', {'form': form})



@login_required
def edit_lead(request, email):
    lead = get_object_or_404(Lead, pk=email)
    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.save()
            return redirect('lead_list')
    else:
        form = LeadForm(instance = lead)
    return render(request, 'lead_form.html', {'form': form})


@login_required
def del_lead(request, email):
    lead = get_object_or_404(Lead, pk=email)
    if request.method == "POST":
        lead.delete()
        return redirect('lead_list')
    return render(request, 'lead_del_conf.html', {'lead': lead})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('lead_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})