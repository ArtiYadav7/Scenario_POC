import json


def load_scenario(file_path):
    """
    Load scenario JSON file
    """

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def get_node(
        scenario,
        node_id
):
    """
    Get a specific node
    """

    for node in scenario["nodes"]:

        if node["node_id"] == node_id:
            return node

    return None


def process_choice(
        scenario,
        current_node_id,
        selected_choice_id
):
    """
    Process learner choice
    """

    node = get_node(
        scenario,
        current_node_id
    )

    if not node:
        return None

    for choice in node["choices"]:

        if choice["choice_id"] == selected_choice_id:

            return {
                "consequence": choice["consequence"],
                "next_node": choice["next_node"],
                "competency_effects": choice["competency_effects"]
            }

    return None


def is_end_node(node_id):
    """
    Check if scenario ended
    """

    return node_id.upper().startswith("END")

    