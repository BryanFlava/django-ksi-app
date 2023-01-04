from django import forms
from hello.models import Posr

class classform(forms.ModelForm):
    class Meta:
        model = Posr
        fields = [
            'title',
            'body',
            'email',
        ]

    widget={
        'title': forms.TextInput(
            attrs = {
                'class' : 'form',
                'placeholder' : 'Masukan Judul',
            }
        )
    }

    def clean_title(self):
        ji = self.cleaned_data.get('title')

        if ji == "Rasis":
            raise forms.ValidationError("Cant post Rasis")

        return ji