def build_debrief_prompt(
    scenario_name,
    outcome,
    strengths,
    improvements
):

    return f"""
Scenario:
{scenario_name}

Outcome:
{outcome}

Strengths:
{', '.join(strengths)}

Areas to Improve:
{', '.join(improvements)}

Provide:

1. Summary
2. What learner did well
3. What learner should improve
4. Workplace tip
5. Reflection question
"""

