from django.shortcuts import render
from .models import Lead
from .forms import LeadForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')



def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'lead_list.html', {'leads': leads})


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


def del_lead(request, email):
    lead = get_object_or_404(Lead, pk=email)
    if request.method == "POST":
        lead.delete()
        return redirect('lead_list')
    return render(request, 'lead_del_conf.html', {'lead': lead})