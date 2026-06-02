def update_scores(
        current_scores,
        competency_effects
):
    """
    Update learner competency scores
    """

    for metric, value in competency_effects.items():

        current_scores[metric] = (
            current_scores.get(metric, 0)
            + value
        )

    return current_scores


def calculate_final_score(scores):
    """
    Sum all competency scores
    """

    return sum(scores.values())


def generate_debrief(
        outcome,
        scores
):
    """
    Generate final learner feedback
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