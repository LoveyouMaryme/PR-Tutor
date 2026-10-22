from github_client import build_headers, build_pr_files_url


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
