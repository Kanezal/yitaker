from django.shortcuts import render

from user_profile.models import Profile
from django.contrib.auth.models import User


def base_ctx() -> dict:
    return {
        "nav": {
            "О нас": {
                "link": "main_page"
            },
            "Планы на будущее": {
                "link": "future_plans"
            },
        }
    }


def main_page(request):
    ctx = base_ctx()
    return render(request, "main_page.html", ctx)


def future_plans(request):
    ctx = base_ctx()
    return render(request, "future_plans.html", ctx)

