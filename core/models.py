from django.db import models
from django.urls import reverse


class Candidate(models.Model):
    POSITION_CHOICES = [
        ("PRESIDENT", "President"),
        ("VP-INTERNAL", "VP-Internal"),
        ("VP-EXTERNAL", "VP-External"),
        ("SECRETARY", "Secretary"),
        ("ASST. SECRETARY", "Asst. Secretary"),
        ("TREASURER", "Treasurer"),
        ("AUDITOR", "Auditor"),
        ("ASST. AUDITOR", "Asst. Auditor"),
        ("PROJECT MANAGER", "Project Manager"),
        ("PRO", "PRO"),
        ("ECO-WARRIOR", "Eco-Warrior"),
        ("2ND YEAR REPRESENTATIVE", "2nd Year Representative"),
    ]

    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    position = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES,
    )
    photo = models.CharField(
        max_length=255,
        blank=True,
    )
    hierarchy_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["hierarchy_order", "id"]

    def __str__(self):
        return f"{self.name} — {self.position}"

    def get_absolute_url(self):
        return reverse(
            "core:candidate-detail",
            kwargs={"slug": self.slug},
        )


class CandidateCredential(models.Model):
    EDUCATION_LEVEL_CHOICES = [
        ("ELEMENTARY", "Elementary"),
        ("JUNIOR HIGH", "Junior High School"),
        ("SENIOR HIGH", "Senior High School"),
        ("COLLEGE", "College"),
        ("GENERAL", "General"),
    ]

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="credentials",
    )
    education_level = models.CharField(
        max_length=30,
        choices=EDUCATION_LEVEL_CHOICES,
    )
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = [
            "education_level",
            "order",
            "id",
        ]

    def __str__(self):
        return f"{self.candidate.name} — {self.title}"


class CandidatePlatform(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="platforms",
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.candidate.name} — {self.title}"


class OverallPlatform(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.category} — {self.title}"