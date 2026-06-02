import uuid

sessions = {}


def create_session(scenario_id):

    session_id = str(uuid.uuid4())

    sessions[session_id] = {
        "scenario_id": scenario_id,
        "current_node": None,
        "scores": {},
        "history": []
    }

    return session_id


def get_session(session_id):

    return sessions.get(session_id)


def update_session(
        session_id,
        current_node,
        scores
):

    if session_id in sessions:

        sessions[session_id]["current_node"] = current_node

        sessions[session_id]["scores"] = scores


def add_history(
        session_id,
        history_item
):

    if session_id in sessions:

        sessions[session_id]["history"].append(
            history_item
        )