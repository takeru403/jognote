from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('blog-home')
  else:
    form = UserCreationForm()
  return render(request, 'account/signup.html', {'form': form})




# Create your views here.
