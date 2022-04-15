from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView
from owner.models import Mobiles
from customer.forms import UserRegistrationForm, LoginForm, PasswordResetForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from customer.models import Cart
from customer.decorators import sign_in_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(sign_in_required, name="dispatch")
class CustomerIndex(ListView):
    model = Mobiles
    template_name = "cust_home.html"
    context_object_name = "mobiles"


# class CustomerIndex(View):
#     def get(self, request, *args, **kwargs):
#         qs = Mobiles.objects.all()
#         return render(request, "cust_home.html", {"mobiles": qs})


class SignUPView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "signup.html"
    success_url = reverse_lazy("sign in")


# class SignUPView(View):
#     def get(self, request, *args, **kwargs):
#         form = UserRegistrationForm()
#         return render(request, "signup.html", {"form": form})
#
#     def post(self, request, *args, **kwargs):
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("sign in")
#         else:
#             return render(request, "signup.html", {"form": form})


class SigninView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "signin.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                print("login succes")
                login(request, user)
                return redirect("custhome")
            else:
                print("login failed")
                return render(request, "signin.html", {"form": form})


@sign_in_required
def signout(request, *args, **kwargs):
    logout(request)
    return redirect("sign in")


@method_decorator(sign_in_required, name="dispatch")
class PasswordReset(View):
    def get(self, request, *args, **kwargs):
        form = PasswordResetForm()
        return render(request, "password_reset.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get("old_password")
            new_password = form.cleaned_data.get("new_password")
            user = authenticate(request, username=request.user, password=old_password)
            if user:
                user.set_password(new_password)
                user.save()
                return redirect("sign in")
            else:
                return render(request, "password_reset.html", {"form": form})

        else:
            return render(request, "password_reset.html", {"form": form})


@sign_in_required
def add_to_cart(request, *args, **kwargs):
    mobile = Mobiles.objects.get(id=kwargs["id"])
    user = request.user
    cart = Cart(product=mobile, user=user)
    cart.save()
    return redirect("custhome")


@method_decorator(sign_in_required, name="dispatch")
class ViewMyCart(ListView):
    model = Cart
    template_name = "my_cart.html"
    context_object_name = "carts"

    def get_queryset(self):
        qs = Cart.objects.filter(user=self.request.user)
        return qs
