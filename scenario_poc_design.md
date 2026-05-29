{
    "scenario_id": "...",

    "target_icp": "...",

    "competencies": [
        "communication",
        "problem_solving",
        "professionalism"
    ],

    "decision_tree": [...]
}

1:  Universal Rubric
communication
problem_solving
professionalism
critical_thinking
ownership

2: ICP-Specific Rubrics
Delivery Partner:
customer_satisfaction

Sales:
objection_handling

Software Engineer:
technical_decision_making


1. Scenario JSON Schem

{
    "scenario_id": "DELIVERY_001",
    "scenario_name": "Customer Not Receiving Order",

    "target_icp": "delivery_partner",

    "learning_objective": [
        "Customer Communication",
        "Problem Solving",
        "Professionalism"
    ],

    "initial_situation": {
        "description": "Customer cannot locate delivery partner."
    },

    "decision_tree": [],

    "scoring_rubric": {},

    "debrief_template": {}
}

2. Node Schema

{
    "node_id": "D1",

    "situation": "Customer says he cannot find you.",

    "choices": [
        {
            "choice_id": "A",
            "text": "Call Customer",
            "next_node": "D2A",

            "score_delta": {
                "communication": 5,
                "problem_solving": 3
            }
        },

        {
            "choice_id": "B",
            "text": "Mark Customer Unavailable",
            "next_node": "D2B",

            "score_delta": {
                "customer_satisfaction": -5
            }
        }
    ]
}


3. Rubric Schema

{
    "customer_satisfaction": {
        "weight": 25
    },

    "professionalism": {
        "weight": 25
    },

    "policy_compliance": {
        "weight": 20
    },

    "problem_solving": {
        "weight": 15
    },

    "communication": {
        "weight": 15
    }
}

4. Final Debrief Schema

{
    "final_score": 82,

    "outcome": "RECOVERED",

    "strengths": [
        "Good customer communication",
        "Professional handling"
    ],

    "improvements": [
        "Escalate earlier",
        "Avoid assumptions"
    ],

    "recommended_behavior": "...",

    "real_world_transfer": "..."
}