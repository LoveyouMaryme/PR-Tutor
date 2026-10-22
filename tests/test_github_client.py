import httpx

from github_client import build_headers, build_pr_files_url, list_pull_request_files


def test_list_pull_request_files_success(monkeypatch):

    fake_files = [
        {"filename": "main.py", "status": "modified"},
        {"filename": "tests.py", "status": "added"},
    ]

    def fake_get(url, headers, timeout):

        # TODO 1 : vérifier que l'URL correspond
        assert (
            url
            == "https://api.github.com/repos/LoveyouMaryme/AnimeDashboard/pulls/42/files"
        )

        # TODO 2 : vérifier que Authorization
        assert headers.get("Authorization") == "Bearer fake-token"

        # TODO 3 : vérifier que timeout vaut 10.0
        assert timeout == 10.0

        return httpx.Response(
            status_code=200,
            json=fake_files,
            request=httpx.Request("GET", url),
        )

    # TODO 1 : remplacer httpx.get par fake_get
    monkeypatch.setattr("httpx.get", fake_get)

    # TODO 2 : appeler list_pull_request_files()
    files = list_pull_request_files("LoveyouMaryme", "AnimeDashboard", 42, "fake-token")

    # TODO 3 : vérifier que le résultat correspond à fake_files
    assert files == fake_files


def test_url_builder():
    url = build_pr_files_url("Love", "Tutor", 42)

    assert url == "https://api.github.com/repos/Love/Tutor/pulls/42/files"


def test_headers_builder():

    headers = build_headers("fake-token-123")

    assert headers == {
        "Authorization": "Bearer fake-token-123",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    assert headers["Authorization"] == "Bearer fake-token-123"
    assert headers["Accept"] == "application/vnd.github+json"
    assert headers["X-GitHub-Api-Version"] == "2022-11-28"
