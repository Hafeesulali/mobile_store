from django import forms
from owner.models import Mobiles


# class MobileForms(forms.Form):
#     mobile_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     mobile_brand = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     price = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
#     number_of_pieces = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
#
#     def clean(self):
#         cleaned_data = super().clean()
#         price = cleaned_data.get("price")
#         number_of_pieces = cleaned_data.get("number_of_pieces")
#         if price < 0:
#             msg = "invalid input"
#             self.add_error("price", msg)
#         if number_of_pieces < 0:
#             msg = "invalid input"
#             self.add_error("number_of_pieces", msg)


class MobileForms(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = ["mobile_name",
                  "mobile_brand",
                  "price",
                  "number_of_pieces",
                  "images"
                  ]
        widgets = {
            "mobile_name": forms.TextInput(attrs={"class": "form-control"}),
            "mobile_brand": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "number_of_pieces": forms.NumberInput(attrs={"class": "form-control"}),
            "images": forms.FileInput(attrs={"class": "form-control"}),

        }
