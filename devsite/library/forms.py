from django import forms

class MusicItemForm(forms.Form):
    inventory_num = forms.CharField(
        max_length=20, required=False,
        widget=forms.TextInput(attrs={
        })
    )
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
        })
    )
    composer_last = forms.CharField(
        max_length=255, required=False,
        widget=forms.TextInput(attrs={
        })
    )
    composer_first = forms.CharField(
        max_length=255, required=False,
        widget=forms.TextInput(attrs={
        })
    )
    arranger_last = forms.CharField(
        max_length=255, required=False,
        widget=forms.TextInput(attrs={
        })
    )
    arranger_first = forms.CharField(
        max_length=255, required=False,
        widget=forms.TextInput(attrs={
        })
    )
    arranger_first = forms.CharField(
        max_length=255, required=False,
        widget=forms.TextInput(attrs={
        })
    )
    ensemble = forms.CharField(
        max_length=255, required=False,
        widget=forms.TextInput(attrs={
        })
    )
    style = forms.CharField(
        max_length=255, required=False,
        widget=forms.TextInput(attrs={
        })
    )
    difficulty = forms.CharField(
        max_length=255, required=False,
        widget=forms.TextInput(attrs={
        })
    )
    rating = forms.CharField(
        max_length=255, required=False,
        widget=forms.TextInput(attrs={
        })
    )
    last_performed = forms.CharField(
        max_length=255, required=False,
        widget=forms.TextInput(attrs={
        })
    )
    organized = forms.BooleanField(required=False,
        )

    notes = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
        })
    )
