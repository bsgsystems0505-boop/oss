from django.contrib import admin

from .models import (
    Candidate,
    CandidateCredential,
    CandidatePlatform,
    OverallPlatform,
)


class CandidateCredentialInline(admin.TabularInline):
    model = CandidateCredential
    extra = 1
    ordering = ("education_level", "order", "id")


class CandidatePlatformInline(admin.TabularInline):
    model = CandidatePlatform
    extra = 1
    ordering = ("order", "id")


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "position",
        "hierarchy_order",
    )
    list_filter = ("position",)
    search_fields = ("name",)
    prepopulated_fields = {
        "slug": ("name",),
    }
    inlines = [
        CandidateCredentialInline,
        CandidatePlatformInline,
    ]
    ordering = ("hierarchy_order", "id")


@admin.register(CandidateCredential)
class CandidateCredentialAdmin(admin.ModelAdmin):
    list_display = (
        "candidate",
        "education_level",
        "category",
        "title",
        "order",
    )
    list_filter = (
        "education_level",
        "category",
    )
    search_fields = (
        "candidate__name",
        "category",
        "title",
        "description",
    )
    ordering = (
        "candidate",
        "education_level",
        "order",
        "id",
    )


@admin.register(OverallPlatform)
class OverallPlatformAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "title",
        "order",
    )
    list_filter = ("category",)
    search_fields = (
        "category",
        "title",
        "description",
    )
    ordering = ("order", "id")