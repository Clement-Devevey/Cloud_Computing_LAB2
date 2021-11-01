from django import forms

class ContactForm(forms.Form):
    couleur = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[('image1', 'Image1'),('image2', 'Image2'),('image3', 'Image3'),('image4', 'Image4'),],)