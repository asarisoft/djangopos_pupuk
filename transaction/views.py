from django.shortcuts import render, redirect
from .forms import TransactionForm

def pos_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos')
    else:
        form = TransactionForm()
    
    context = {'form': form}
    return render(request, 'transaction/pos.html', context)