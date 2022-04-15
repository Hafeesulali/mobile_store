from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView
from owner.forms import MobileForms
from owner.models import Mobiles
from django.urls import reverse_lazy


class AddMobile(CreateView):
    model = Mobiles
    form_class = MobileForms
    template_name = "add_mob.html"
    success_url = reverse_lazy("mobile list")


# class AddMobile(View):
#     def get(self, request):
#         form = MobileForms()
#         return render(request, "add_mob.html", {"form": form})
#
#     def post(self, request):
#         form = MobileForms(request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             # print(form.cleaned_data.get("mobile_name"))
#             # print(form.cleaned_data.get("mobile_brand"))
#             # print(form.cleaned_data.get("price"))
#             # print(form.cleaned_data.get("number_of_pieces"))
#             # qs = Mobiles(
#             #     mobile_name=form.cleaned_data.get("mobile_name"),
#             #     mobile_brand=form.cleaned_data.get("mobile_brand"),
#             #     price=form.cleaned_data.get("price"),
#             #     number_of_pieces=form.cleaned_data.get("number_of_pieces")
#             # )
#             # qs.save()
#             return redirect("mobile list")
#             # return render(request, "add_mob.html", {"msg": "mobile added"})
#         else:
#             return render(request, "add_mob.html", {"form": form})


class MobileList(ListView):
    model = Mobiles
    template_name = "mobile_list.html"
    context_object_name = "mobiles"


# class MobileList(View):
#     def get(self, request):
#         qs = Mobiles.objects.all()
#         return render(request, "mobile_list.html", {"mobiles": qs})


class MobileDetailView(DetailView):
    model = Mobiles
    template_name = "mobile_detail.html"
    context_object_name = "mobile"
    pk_url_kwarg = "id"


#
# class MobileDetailView(View):
#     def get(self, request, *args, **kwargs):
#         qs = Mobiles.objects.get(id=kwargs.get("id"))
#         return render(request, "mobile_detail.html", {"mobile": qs})


class MobileDeleteView(View):
    def get(self, request, *args, **kwargs):
        qs = Mobiles.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("mobile list")


class ChangeMobile(UpdateView):
    model = Mobiles
    template_name = "mobile_edit.html"
    form_class = MobileForms
    success_url = reverse_lazy("mobile list")
    pk_url_kwarg = "id"

# class ChangeMobile(View):
#     def get(self, request, *args, **kwargs):
#         qs = Mobiles.objects.get(id=kwargs.get("id"))
#         form = MobileForms(instance=qs)
#         return render(request, "mobile_edit.html", {"form": form})
#
#     def post(self, request, *args, **kwargs):
#         qs = Mobiles.objects.get(id=kwargs.get("id"))
#         form = MobileForms(request.POST, files=request.FILES, instance=qs)
#         if form.is_valid():
#             form.save()
#             return redirect("mobile list")
