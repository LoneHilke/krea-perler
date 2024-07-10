from django.shortcuts import render, redirect
from django.views import View
from .models import Plade, Runde, Category, Kant, Anmeld, Kugle, Model
from .forms import AnmeldForm

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
      hjerter = Plade.objects.filter(category__name__contains = 'Hjerter')
      stjerne = Plade.objects.filter(category__name__contains = 'Stjerne')
      jul = Plade.objects.filter(category__name__contains = 'Jul')
      andet = Plade.objects.filter(category__name__contains = 'Andet')
      hjerte = Plade.objects.filter(kant__name__contains = 'Hjerte')
      stjern = Plade.objects.filter(kant__name__contains = 'Stjerne')
      rund = Plade.objects.filter(kant__name__contains = 'Rund')
      firkant = Plade.objects.filter(kant__name__contains = 'firkant')
      sekskant = Plade.objects.filter(kant__name__contains = 'sekskant')
      form = AnmeldForm()
      anmeld=Anmeld.objects.all()
      bordskåner = Kugle.objects.filter(model__name__contains = 'Bordskåner')
      armbånd = Kugle.objects.filter(model__name__contains = 'Armbånd')
      skål = Kugle.objects.filter(model__name__contains = 'Skål')
      other = Kugle.objects.filter(model__name__contains = 'Other')
    
      context = {
          'stjerne': stjerne,
          'hjerter': hjerter,
          'jul': jul,
          'andet': andet,
          'hjerte': hjerte,
          'rund': rund,
          'firkant': firkant,
          'sekskant': sekskant,
          'stjern': stjern,
          'form': form,
          'anmeld': anmeld,
          'bordskåner': bordskåner,
          'armbånd': armbånd,
          'skål': skål,
          'other': other
        } 
      return render(request, 'sjov/index.html', context)
    
    def post(self, request, *args, **kwargs):
    
        form = AnmeldForm(request.POST)
        if form.is_valid():
            form.save()
        
            return redirect('/')
        
        anmeld = Anmeld.objects.all()
        context = {
        
            'form': form,
            'anmeld': anmeld,
        
        }
        return render(request, 'sjov/index.html', context)