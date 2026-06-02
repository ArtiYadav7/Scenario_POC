from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import json
from pathlib import Path

from models.scenario_models import Scenario

from services.session_manager import (                #new
    create_session,
    get_session,
    update_session,
    add_history
)

from services.evaluater import (                #new
    update_scores,
    generate_debrief
)


from services.scenario_engine import (
    get_node,
    process_choice,
    get_outcome_by_id
)

app = FastAPI(
    title="Vidya Scenario Engine POC",
    description="Branching workplace simulation engine",
    version="1.0.0"
)

BASE_DIR = Path(__file__).parent


class ChoiceRequest(BaseModel):

    session_id: str

    selected_choice_id: str

class StartScenarioRequest(BaseModel):               #new
    scenario_id: str

def get_scenario_path(scenario_id: str):

    scenario_map = {
        "DELIVERY_001":
            BASE_DIR / "scenarios" / "delivery_partner" / "DELIVERY_001.json",

        "SWE_001":
            BASE_DIR / "scenarios" / "software_engineer" / "SWE_001.json"
    }

    return scenario_map.get(scenario_id)


@app.get("/")
def home():

    return {
        "message": "Vidya Scenario Engine POC Running"
    }


@app.get("/scenario/{scenario_id}")
def get_scenario(scenario_id: str):
    
    file_path = get_scenario_path(scenario_id)
    print("LOADED FILE:", file_path)
    if not file_path:
        raise HTTPException(
            status_code=404,
            detail="Scenario not found"
        )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        data= json.load(f)
    scenario = Scenario.model_validate(data)
    return scenario.model_dump()    
    print(data)    


@app.post("/scenario/start")              #new
def start_scenario(
        request: StartScenarioRequest
):
    
    file_path = get_scenario_path(
        request.scenario_id
    )
    print("START FILE:", file_path)
    if not file_path:

        raise HTTPException(
            status_code=404,
            detail="Scenario not found"
        )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)
    scenario = Scenario.model_validate(data)
    scenario = scenario.model_dump()
    
    session_id = create_session(
        request.scenario_id
    )

    start_node_id = scenario["start_node"]

    update_session(
    session_id,
    start_node_id,
    {}
    )

    start_node = get_node(
        scenario,
        start_node_id
    )

    return {

        "session_id": session_id,

        "scenario_id":
        request.scenario_id,

        "current_node":
        start_node_id,

        "state":
        start_node
    }

@app.post("/scenario/choice")
def choose(choice_request: ChoiceRequest):

    session = get_session(
        choice_request.session_id
    )

    if not session:

        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    scenario_id = session["scenario_id"]

    current_node_id = session["current_node"]

    scores = session["scores"]

    file_path = get_scenario_path(
        scenario_id
    )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)
    scenario = Scenario.model_validate(data)
    scenario = scenario.model_dump()

    result = process_choice(
    scenario,
    current_node_id,
    choice_request.selected_choice_id
)

    if not result:

      raise HTTPException(
        status_code=400,
        detail="Invalid choice"
    )

    history_item = {

    "node_id":
    current_node_id,

    "choice_id":
    choice_request.selected_choice_id,

    "choice_text":
    result["choice_text"],

    "reflection":
    result["reflection"],

    "competency_effects":
    result["competency_effects"]
}

    add_history(
    choice_request.session_id,
    history_item
)
    
    

    scores = update_scores(
        scores,
        result["competency_effects"]
    )

    update_session(
        choice_request.session_id,
        result["next_node"],
        scores
    )

    next_node = get_node(
        scenario,
        result["next_node"]
    )

    return {

        "consequence":
        result["consequence"],

        "reflection":
        result["reflection"],

        "competency_effects":
        result["competency_effects"],

        "current_scores":
        scores,

        "next_node":
        result["next_node"],

        "next_state":
        next_node
    }

@app.get("/scenario/result/{session_id}")
def get_result(session_id: str):

    session = get_session(session_id)

    if not session:

        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    current_node = session["current_node"]

    if not current_node.startswith("END_"):

        raise HTTPException(
            status_code=400,
            detail="Scenario not completed"
        )

    outcome_id = current_node.replace(
        "END_",
        ""
    )

    scenario_id = session["scenario_id"]

    file_path = get_scenario_path(
        scenario_id
    )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)
    scenario = Scenario.model_validate(data)
    scenario = scenario.model_dump()

    outcome = get_outcome_by_id(
        scenario,
        outcome_id
    )

    debrief = generate_debrief(
        outcome_id,
        session["scores"]
    )

    return {

        "outcome":
        outcome_id,

        "title":
        outcome["title"],

        "history":
        session["history"],

        "description":
        outcome["description"],

        "business_impact":
        outcome["business_impact"],

        "final_score":
        debrief["final_score"],

        "strengths":
        debrief["strengths"],

        "improvements":
        debrief["improvements"],

        "summary":
        debrief["summary"]
    }