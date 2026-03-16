# Candidate context/profile for personalized interview assessment

CANDIDATE_CONTEXT_TEMPLATE = """
## Candidate Profile

**Name:** {name}
**Experience Level:** {experience_level}
**Target Role:** {target_role}
**Tech Stack:** {tech_stack}
**Areas of Interest:** {interests}
**Years of Experience:** {years_of_experience}

## Interview Focus Areas
{focus_areas}

## Additional Notes
{additional_notes}
"""

INTERVIEW_TYPES = {
    "interest": {
        "name": "Interest-Based Questions",
        "description": "Questions based on candidate's interests and background"
    },
    "scenario": {
        "name": "Scenario-Based Questions",
        "description": "Real-world problem-solving scenarios"
    },
    "system_design": {
        "name": "System Design",
        "description": "Architecture and design questions"
    },
    "leetcode": {
        "name": "DSA/LeetCode Style",
        "description": "Data structures and algorithms coding questions"
    }
}

EXPERIENCE_LEVELS = ["Fresher", "Junior (1-2 years)", "Mid (3-5 years)", "Senior (5+ years)", "Staff/Principal"]

DEFAULT_FOCUS_AREAS = [
    "Data Structures & Algorithms",
    "System Design",
    "Problem Solving",
    "Code Quality",
    "Communication Skills"
]


def build_candidate_context(
    name: str,
    experience_level: str,
    target_role: str,
    tech_stack: list,
    interests: list,
    years_of_experience: int,
    focus_areas: list = None,
    additional_notes: str = ""
) -> str:
    """Build a formatted candidate context string for the LLM."""
    
    if focus_areas is None:
        focus_areas = DEFAULT_FOCUS_AREAS
    
    return CANDIDATE_CONTEXT_TEMPLATE.format(
        name=name,
        experience_level=experience_level,
        target_role=target_role,
        tech_stack=", ".join(tech_stack) if tech_stack else "Not specified",
        interests=", ".join(interests) if interests else "Not specified",
        years_of_experience=years_of_experience,
        focus_areas="\n".join(f"- {area}" for area in focus_areas),
        additional_notes=additional_notes or "None"
    )
