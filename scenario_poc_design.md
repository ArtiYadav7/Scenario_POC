# Scenario POC Design

## Goal

Build a reusable workplace simulation engine where learners make decisions, experience consequences, receive competency scores, and get a final debrief.

The architecture should support multiple ICPs (Ideal Customer Profiles) such as:

* Delivery Partner
* Software Engineer
* Sales Executive
* Customer Support Agent
* Recruiter
* Store Manager

and scale to hundreds of scenarios.

---

# High-Level Architecture

Scenario
↓
State
↓
Decision
↓
Consequence
↓
Competency Update
↓
Outcome
↓
Debrief

---

# Universal Competencies

These competencies can be used across all ICPs.

```json
[
  "communication",
  "problem_solving",
  "professionalism",
  "critical_thinking",
  "ownership"
]
```

---

# ICP-Specific Competencies

### Delivery Partner

```json
[
  "customer_satisfaction"
]
```

### Software Engineer

```json
[
  "technical_decision_making",
  "collaboration"
]
```

### Sales Executive

```json
[
  "objection_handling",
  "negotiation"
]
```

---

# Scenario Schema

```json
{
  "scenario_id": "DELIVERY_001",

  "scenario_name": "Customer Cannot Find You",

  "target_icp": "delivery_partner",

  "role": "Delivery Partner",

  "industry": "Logistics",

  "difficulty": "Beginner",

  "estimated_duration": 7,

  "learning_skills": [
    "communication",
    "problem_solving",
    "professionalism"
  ],

  "start_node": "D1",

  "nodes": [],

  "outcomes": []
}
```

---

# State (Node) Schema

A state represents the learner's current situation.

```json
{
  "node_id": "D1",

  "state_type": "customer_confused",

  "situation": "Customer says he cannot locate you.",

  "choices": []
}
```

Examples:

```text
customer_confused
customer_angry
customer_recovered
critical_bug_detected
production_outage
team_review
```

State types are important for:

* analytics
* learner state tracking
* tutor intervention
* mastery systems

---

# Choice Schema

Each decision must create a consequence.

```json
{
  "choice_id": "A",

  "text": "Call customer",

  "consequence":
  "Customer shares the correct landmark and becomes cooperative.",

  "next_node": "D2A",

  "competency_effects": {
    "communication": 5,
    "problem_solving": 3
  }
}
```

---

# Competency Effects

Competencies are updated after every learner decision.

```json
{
  "communication": 5,

  "problem_solving": 3,

  "professionalism": 2
}
```

This replaces the older:

```json
{
  "score_delta": 10
}
```

approach.

---

# Outcome Schema

Every scenario must define explicit outcomes.

```json
{
  "outcome_id": "BEST",

  "title": "Positive Customer Experience",

  "description":
  "Customer received the order successfully and appreciated the interaction.",

  "business_impact":
  "5-star rating"
}
```

Examples:

```text
BEST
AVERAGE
POOR
```

---

# Scoring Framework

Scores are accumulated from competency effects.

Example:

```json
{
  "communication": 8,

  "problem_solving": 5,

  "professionalism": 10
}
```

Final score:

```python
sum(scores.values())
```

Outcome mapping:

```text
20+   → BEST
10-19 → AVERAGE
<10   → POOR
```

---

# Debrief Schema

```json
{
  "outcome": "BEST",

  "final_score": 26,

  "strengths": [
    "communication",
    "professionalism"
  ],

  "improvements": [],

  "summary":
  "Strong customer communication and professional handling."
}
```

---

# Scenario Quality Validation

Every scenario should satisfy:

### 1. State Change

Did the situation change because of the learner's decision?

If NO:

Scenario is weak.

---

### 2. Branching Outcomes

Can two learners reach different outcomes?

If NO:

Scenario is weak.

---

### 3. Consequences

Does every choice produce a consequence?

If NO:

Scenario is a quiz.

---

# API Design (Current)

### Get Scenario

```http
GET /scenario/{scenario_id}
```

Example:

```http
GET /scenario/DELIVERY_001
```

---

# API Design (Future)

Start Scenario

```http
POST /scenario/start
```

Submit Choice

```http
POST /scenario/choice
```

Get Result

```http
GET /scenario/result
```

Flow:

Start
↓
Choice
↓
Choice
↓
Choice
↓
Result
↓
Debrief

---

# Current POC Scope

Implemented:

✓ Scenario JSON structure

✓ State-based scenario design

✓ Consequence-driven decisions

✓ Competency scoring

✓ Outcomes

✓ Debrief generation

✓ FastAPI scenario retrieval

Future:

✓ Scenario progression API

✓ Session management

✓ Learner mastery tracking

✓ AI-generated scenario creation

✓ Tutor integration

✓ Analytics pipeline
