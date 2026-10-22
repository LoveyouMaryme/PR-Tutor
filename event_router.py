def route_event(event_name: str, payload: dict) -> str:

    if event_name == "pull_request" and (payload.get("action") == "synchronize" or payload.get("action") == "opened"):
        return "REVIEW_PR"

    elif event_name == "pull_request_review_comment" and payload.get("action") == "created"  and payload.get("comment", {}).get("in_reply_to_id") is not None:
        return "REPLY"
    else:
        return "IGNORE"


