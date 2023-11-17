from django import forms
from .models import Feedback
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox, ReCaptchaV2Invisible

class FeedbackForm(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible(), label=' ')
    
    class Meta:
        model = Feedback
        fields = ['nama', 'kontak', 'pesan']
