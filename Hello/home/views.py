from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from home.models import Contact as ContactModel


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")   # <-- recommended


def Flavour(request):
    return render(request, "Flavour.html")   # ← ONLY THIS
  # <-- recommended


def Home(request):
    return render(request, "Home.html")      # <-- recommended


def contactPage(request):
    return render(request, "Contact.html")   # <-- FIXED (Correct file name)


def contactSubmit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        ContactModel.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        messages.success(request, "Message sent successfully!")
        return redirect("contact")

    return redirect("contact")
