from event_router import route_event


def test_pr_synchronize():
    assert route_event(
        "pull_request",
        {"action": "synchronize"}
    ) == "REVIEW_PR"


def test_pr_opened():
    assert route_event(
        "pull_request",
        {"action": "opened"}
    ) == "REVIEW_PR"


def test_unknown_event():
    assert route_event(
        "push",
        {}
    ) == "IGNORE"

def test_other_event_same_action():
    assert route_event(
        "issues",
        {"action": "synchronize"}
    ) == "IGNORE"


def test_reply_to_comment():
    payload = {
        "action": "created",
        "comment": {
            "id": 789,
            "in_reply_to_id": 456
        }
    }

    assert route_event(
        "pull_request_review_comment",
        payload
    ) == "REPLY"


def test_new_comment_without_parent():
    payload = {
        "action": "created",
        "comment": {"id": 789}
    }

    assert route_event(
        "pull_request_review_comment",
        payload
    ) == "IGNORE"


def test_missing_comment():
    assert route_event(
        "pull_request_review_comment",
        {"action": "created"}
    ) == "IGNORE"

import pytest

from event_router import route_event


@pytest.mark.parametrize(
    "event_name, payload, expected",
    [
        ("pull_request", {"action": "synchronize"}, "REVIEW_PR"),
        ("pull_request", {"action": "opened"}, "REVIEW_PR"),
        ("pull_request_review_comment", {
            "action": "created",
            "comment": {"id": 789, "in_reply_to_id": 456}
        }, "REPLY"),
        ("pull_request_review_comment", {
            "action": "created",
            "comment": {"id": 900}
        }, "IGNORE"),
        ("pull_request_review_comment", {
            "action": "deleted",
            "comment": {"in_reply_to_id": 456}
        }, "IGNORE"),
        ("push", {}, "IGNORE"),
    ],
)
def test_route_event(event_name, payload, expected):
    assert route_event(event_name, payload) == expected