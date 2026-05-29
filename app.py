from fastapi import FastAPI, HTTPException
import json
from pathlib import Path

app = FastAPI(
    title="Vidya Scenario Engine POC",
    description="Branching workplace simulation engine",
    version="1.0.0"
)

BASE_DIR = Path(__file__).parent


@app.get("/")
def home():
    return {
        "message": "Vidya Scenario Engine POC Running"
    }


@app.get("/scenario/{scenario_id}")
def get_scenario(scenario_id: str):

    scenario_map = {
        "DELIVERY_001": BASE_DIR / "scenarios" / "delivery_partner" / "DELIVERY_001.json",
        "SWE_001": BASE_DIR / "scenarios" / "software_engineer" / "SWE_001.json"
    }

    file_path = scenario_map.get(scenario_id)

    if not file_path:
        raise HTTPException(
            status_code=404,
            detail="Scenario not found"
        )

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)