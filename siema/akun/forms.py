from django import forms
from django.conf import settings
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible


class LoginForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible(), label=' ')
