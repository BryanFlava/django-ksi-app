from django.core.exceptions import ValidationError

def title_val(value):
    inputjudul = value
    if inputjudul == "Root":
        m = "Can't input" + inputjudul + "as title!"
        raise ValidationError(m)