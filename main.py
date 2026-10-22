from event_router import route_event
from github_event_loader import load_github_event


def main():

    event_name, payload = load_github_event()

    action = route_event(event_name, payload)

    print(action)


if __name__ == "__main__":
    main()
