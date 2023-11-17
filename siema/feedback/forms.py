from django import forms
from .models import Feedback
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class FeedbackForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    
    class Meta:
        model = Feedback
        fields = ['nama', 'kontak', 'pesan']
