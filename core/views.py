from django.shortcuts import get_object_or_404, render

from .models import Candidate, CandidateCredential, OverallPlatform


def get_candidate_hierarchy():
    candidates = list(
        Candidate.objects
        .prefetch_related(
            "platforms",
            "credentials",
        )
        .all()
    )

    candidate_by_position = {
        "president": next(
            (
                candidate
                for candidate in candidates
                if candidate.position == "PRESIDENT"
            ),
            None,
        ),
        "vp_internal": next(
            (
                candidate
                for candidate in candidates
                if candidate.position == "VP-INTERNAL"
            ),
            None,
        ),
        "vp_external": next(
            (
                candidate
                for candidate in candidates
                if candidate.position == "VP-EXTERNAL"
            ),
            None,
        ),
        "secretary": next(
            (
                candidate
                for candidate in candidates
                if candidate.position == "SECRETARY"
            ),
            None,
        ),
        "assistant_secretary": next(
            (
                candidate
                for candidate in candidates
                if candidate.position == "ASST. SECRETARY"
            ),
            None,
        ),
        "treasurer": next(
            (
                candidate
                for candidate in candidates
                if candidate.position == "TREASURER"
            ),
            None,
        ),
        "auditor": next(
            (
                candidate
                for candidate in candidates
                if candidate.position == "AUDITOR"
            ),
            None,
        ),
        "assistant_auditor": next(
            (
                candidate
                for candidate in candidates
                if candidate.position == "ASST. AUDITOR"
            ),
            None,
        ),
        "project_manager": next(
            (
                candidate
                for candidate in candidates
                if candidate.position == "PROJECT MANAGER"
            ),
            None,
        ),
        "pro": next(
            (
                candidate
                for candidate in candidates
                if candidate.position == "PRO"
            ),
            None,
        ),
        "eco_warrior": next(
            (
                candidate
                for candidate in candidates
                if candidate.position == "ECO-WARRIOR"
            ),
            None,
        ),
        "representative": next(
            (
                candidate
                for candidate in candidates
                if candidate.position == "2ND YEAR REPRESENTATIVE"
            ),
            None,
        ),
    }

    return candidates, candidate_by_position


def home(request):
    candidates, candidate_by_position = get_candidate_hierarchy()

    return render(
        request,
        "core/home.html",
        {
            "candidates": candidates,
            "candidate_by_position": candidate_by_position,
        },
    )


def about(request):
    candidates, candidate_by_position = get_candidate_hierarchy()

    return render(
        request,
        "core/about.html",
        {
            "candidates": candidates,
            "candidate_by_position": candidate_by_position,
        },
    )


def platforms(request):
    overall_platforms = OverallPlatform.objects.all()

    return render(
        request,
        "core/platforms.html",
        {
            "overall_platforms": overall_platforms,
        },
    )


def candidate_detail(request, slug):
    candidate = get_object_or_404(
        Candidate.objects.prefetch_related(
            "platforms",
            "credentials",
        ),
        slug=slug,
    )

    credentials = list(candidate.credentials.all())

    credential_groups = [
        (
            "Junior High School",
            [c for c in credentials if c.education_level == "JUNIOR HIGH"],
        ),
        (
            "Senior High School",
            [c for c in credentials if c.education_level == "SENIOR HIGH"],
        ),
        (
            "College",
            [c for c in credentials if c.education_level == "COLLEGE"],
        ),
    ]

    return render(
        request,
        "core/candidate_detail.html",
        {
            "candidate": candidate,
            "credentials": credentials,
            "credential_groups": credential_groups,
        },
    )