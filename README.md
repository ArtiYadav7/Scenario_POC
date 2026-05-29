# Vidya Scenario Engine POC

## Overview

This project is a Proof of Concept (POC) for Vidya v3 Scenario-Based Learning.

The objective is to simulate real-world workplace situations where learners make decisions, experience consequences, receive scores, and get feedback.

Unlike quizzes, every learner choice changes the scenario path and outcome.

---

## Features

- Branching scenario engine
- Multiple decision points
- Consequence-driven learning
- ICP-specific scenarios
- Scoring framework
- JSON-based scenario definitions
- FastAPI backend

---

## Project Structure

```text
Scenario_POC/
│
├── app.py
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
    ├── delivery_partner/
    │   └── DELIVERY_001.json
    │
    └── software_engineer/
        └── SWE_001.json
```

---

## Scenario Structure

Each scenario follows:

```json
{
  "scenario_id": "",
  "scenario_name": "",
  "target_icp": "",
  "objective": [],
  "start_node": "",
  "nodes": []
}
```

Each node contains:

```json
{
  "node_id": "",
  "situation": "",
  "choices": []
}
```

Each choice contains:

```json
{
  "choice_id": "",
  "text": "",
  "next_node": "",
  "score_delta": {}
}
```

---

## Current Scenarios

### DELIVERY_001

Customer Cannot Find You

Target ICP:
Delivery Partner

Skills:
- Communication
- Problem Solving
- Professionalism
- Customer Satisfaction

---

### SWE_001

Software Engineer Workplace Scenario

Target ICP:
Software Engineer

Skills:
- Communication
- Ownership
- Problem Solving
- Professionalism

---

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn app:app --reload
```

Swagger Docs:

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

## Future Improvements

- Scenario state management
- LLM-generated consequences
- Dynamic branching
- AI tutor feedback
- Scoring dashboard
- Learner mastery integration
- Layer A integration
- Event capture integration

---

## Vidya v3 Alignment

This POC aligns with:

- Scenario Learning Framework
- ICP-specific personalization
- Decision-based learning
- State-Out event capture
- Future Learner State integration

---

# Author
Arti Yadav