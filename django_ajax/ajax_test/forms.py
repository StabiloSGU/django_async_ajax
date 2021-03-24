from django.forms import ModelForm, HiddenInput
from ajax_test.models import FileUpload

class AjaxForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = '__all__'
        widgets = {
            'status': HiddenInput(),
        }