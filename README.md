# Vidya Scenario Engine POC

## Overview

This project is a Proof of Concept (POC) for Vidya v3 Scenario-Based Learning.

The goal is to simulate real-world workplace situations where learners make decisions, experience consequences, develop competencies, and receive outcome-based feedback.

Unlike traditional quizzes, learner choices directly influence scenario states, outcomes, and competency development.

---

## Core Learning Flow

```text
Scenario
    ↓
State
    ↓
Decision
    ↓
Consequence
    ↓
Competency Effects
    ↓
Outcome
    ↓
Debrief
```

Each learner can reach different outcomes based on their decisions.

---

## Key Features

* State-based scenario architecture
* Branching decision trees
* Consequence-driven learning
* Competency-based scoring
* Multiple ICP support
* Outcome-driven debriefs
* JSON scenario definitions
* FastAPI backend
* Future-ready for AI Tutor integration

---

## Project Structure

```text
Scenario_POC/
│
├── app.py
├── prompt.py
├── requirements.txt
├── README.md
│
├── models/
│   └── scenario_model.py
│
├── services/
│   ├── scenario_engine.py
│   └── evaluator.py
│
└── scenarios/
    │
    ├── delivery_partner/
    │   └── DELIVERY_001.json
    │
    └── software_engineer/
        └── SWE_001.json
```

---
## Scenario Lifecycle

Scenario Loaded
↓
State Presented
↓
Learner Chooses Action
↓
Consequence Applied
↓
Competencies Updated
↓
Next State Loaded
↓
Outcome Determined
↓
Debrief Generated

The learner progresses through a branching decision tree where each choice updates competency scores and influences the final outcome.


## Scenario Architecture

Each scenario contains:

```json
{
  "scenario_id": "",
  "scenario_name": "",
  "target_icp": "",
  "role": "",
  "industry": "",
  "difficulty": "",
  "estimated_duration": 0,
  "learning_skills": [],
  "start_node": "",
  "nodes": [],
  "outcomes": []
}
```

---

## State Schema

Each node represents a learning state.

```json
{
  "node_id": "",
  "state_type": "",
  "situation": "",
  "choices": []
}
```

Examples:

* customer_confused
* customer_angry
* customer_recovered
* critical_bug_detected
* production_outage
* team_review

State types allow future analytics, mastery tracking, and learner-state integration.

---

## Choice Schema

```json
{
  "choice_id": "",
  "text": "",
  "consequence": "",
  "next_node": "",
  "competency_effects": {}
}
```

Example:

```json
{
  "choice_id": "A",
  "text": "Call customer",
  "consequence": "Customer shares correct location.",
  "next_node": "D2A",
  "competency_effects": {
    "communication": 5,
    "problem_solving": 3
  }
}
```

---

## Outcome Schema

```json
{
  "outcome_id": "",
  "title": "",
  "description": "",
  "business_impact": ""
}
```

Example:

```json
{
  "outcome_id": "BEST",
  "title": "Positive Customer Experience",
  "description": "Customer received order successfully.",
  "business_impact": "5-star rating"
}
```
## Outcome Calculation Logic

Each learner choice contributes competency effects.

Example:

Communication +5
Problem Solving +3
Professionalism +10

The evaluator aggregates all competency values into a final score.

Current POC Logic:

* BEST → Score ≥ 20
* AVERAGE → Score ≥ 10 and < 20
* POOR → Score < 10

Future versions may use weighted competencies, critical failure paths, and mastery-based evaluation.

---

## Competency Framework

### Universal Competencies

Used across all ICPs.

* Communication
* Problem Solving
* Professionalism
* Critical Thinking
* Ownership

### ICP-Specific Competencies

Delivery Partner

* Customer Satisfaction

Software Engineer

* Technical Decision Making
* Collaboration

Sales Representative

* Objection Handling
* Negotiation

Customer Support

* Conflict Resolution
* Empathy

---

## Current Scenarios

### DELIVERY_001

Customer Cannot Find You

Target ICP:
Delivery Partner

Skills:

* Communication
* Problem Solving
* Professionalism
* Customer Satisfaction

Possible Outcomes:

* BEST
* AVERAGE
* POOR

---

### SWE_001

Production Bug Before Release

Target ICP:
Software Engineer

Skills:

* Technical Decision Making
* Collaboration
* Ownership
* Communication

Possible Outcomes:

* BEST
* AVERAGE
* POOR

---

## Evaluation Engine

The evaluator tracks competency growth throughout the scenario.

Example:

```json
{
  "communication": 8,
  "problem_solving": 5,
  "professionalism": 10
}
```

Final evaluation generates:

```json
{
  "outcome": "BEST",
  "final_score": 23,
  "strengths": [],
  "improvements": [],
  "summary": ""
}
```

---

## Run Locally

Install dependencies

```bash
pip install -r requirements.txt
```

Start FastAPI

```bash
uvicorn app:app --reload
```

Open Swagger

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

```http
GET /
```

### Fetch Scenario

```http
GET /scenario/DELIVERY_001
```

```http
GET /scenario/SWE_001
```

---

## Future API Design

### Start Scenario

```http
POST /scenario/start
```

### Submit Choice

```http
POST /scenario/choice
```

### Get Result

```http
GET /scenario/result
```

---

## Future Enhancements

### Scenario Engine

* Dynamic branching
* Scenario state persistence
* Session management

### Learning Science

* Competency mastery tracking
* Personalized remediation
* Difficulty adaptation

### AI Layer

* AI-generated debriefs
* Tutor feedback generation
* Reflection questions
* Coaching recommendations

### Vidya Integration

* Learner State Service
* Mastery Tracking
* Roadmap Generation
* Event Capture
* Analytics Layer

---

## Vidya v3 Alignment

This POC aligns with:

### Layer A — Learner State

Future competency mastery integration.

### Layer B — Learning Engine

Scenario-based workplace simulations.

### Layer C — State-Out

Decision events and competency outcomes.

```text
Learner
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
```
## Future Event Model

Every learner interaction can be stored as an event.

Example:

{
"event_type": "choice_selected",
"scenario_id": "DELIVERY_001",
"state_type": "customer_confused",
"choice_id": "A",
"timestamp": "2026-05-30T10:30:00Z"
}

This enables:

* Learning analytics
* Competency mastery tracking
* AI coaching
* Personalized recommendations
* Scenario performance insights

---

## Current Status

Completed:

* Scenario Architecture
* State-Based Design
* Branching Logic
* Competency Tracking
* Outcome Modeling
* Evaluation Engine
* FastAPI Integration
* Multiple ICP Support

Planned:

* Scenario Sessions
* Choice APIs
* Result APIs
* AI Debriefs
* Mastery Tracking


---

# Author

Arti Yadav
