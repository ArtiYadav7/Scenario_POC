def update_scores(
        current_scores,
        competency_effects
):
    """
    Update learner scores
    """

    for metric, value in competency_effects.items():

        current_scores[metric] = (
            current_scores.get(metric, 0)
            + value
        )

    return current_scores


def calculate_final_score(scores):
    """
    Sum all scores
    """

    return sum(scores.values())


def get_outcome(final_score):

    if final_score >= 25:
        return "BEST"

    elif final_score >= 10:
        return "AVERAGE"

    return "POOR"


def generate_debrief(scores):
    """
    Create debrief data
    """

    strengths = []
    improvements = []

    for metric, value in scores.items():

        if value >= 8:
            strengths.append(metric)

        elif value < 0:
            improvements.append(metric)

    final_score = calculate_final_score(
        scores
    )

    outcome = get_outcome(
        final_score
    )

    return {
        "outcome": outcome,
        "final_score": final_score,
        "strengths": strengths,
        "improvements": improvements,
        "summary": build_summary(
            outcome,
            strengths,
            improvements
        )
    }


def build_summary(
        outcome,
        strengths,
        improvements
):
    """
    Human-readable feedback
    """

    summary = f"Outcome: {outcome}\n\n"

    if strengths:

        summary += (
            "Strengths: "
            + ", ".join(strengths)
            + "\n"
        )

    if improvements:

        summary += (
            "Needs Improvement: "
            + ", ".join(improvements)
            + "\n"
        )

    return summary