def update_scores(
        current_scores,
        score_delta
):
    """
    Update learner scores
    """

    for metric, value in score_delta.items():

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
    """
    Determine outcome
    """

    if final_score >= 20:
        return "BEST"

    elif final_score >= 10:
        return "AVERAGE"

    else:
        return "POOR"


def generate_debrief(scores):
    """
    Create debrief data
    """

    strengths = []
    improvements = []

    for metric, value in scores.items():

        if value >= 5:
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