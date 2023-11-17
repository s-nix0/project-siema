from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # reCAPTCHA validation
            if form.cleaned_data.get('captcha'):
                form.save()
                messages.success(request, 'Terima kasih atas umpan balik Anda!')
                return redirect('feedback_form')
            else:
                messages.error(request, 'reCAPTCHA tidak valid. Coba lagi.')
        else:
            messages.error(request, 'Ada kesalahan dalam formulir.')
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback_form.html', {'form': form})
