from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import json
from pathlib import Path

from services.scenario_engine import (
    get_node,
    process_choice
)

app = FastAPI(
    title="Vidya Scenario Engine POC",
    description="Branching workplace simulation engine",
    version="1.0.0"
)

BASE_DIR = Path(__file__).parent


class ChoiceRequest(BaseModel):
    scenario_id: str
    current_node_id: str
    selected_choice_id: str


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

        return json.load(f)


@app.post("/scenario/choice")
def choose(choice_request: ChoiceRequest):

    file_path = get_scenario_path(
        choice_request.scenario_id
    )

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

        scenario = json.load(f)

    result = process_choice(
        scenario,
        choice_request.current_node_id,
        choice_request.selected_choice_id
    )

    if not result:
        raise HTTPException(
            status_code=400,
            detail="Invalid choice"
        )

    next_node = get_node(
        scenario,
        result["next_node"]
    )

    return {
        "consequence": result["consequence"],
        "competency_effects": result["competency_effects"],
        "next_node": result["next_node"],
        "next_state": next_node
    }