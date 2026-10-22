import httpx


def build_pr_files_url(owner: str, repo: str, pull_number: int) -> str:
    # TODO : retourner l'URL GitHub correspondante

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"

    return url


def build_headers(token: str) -> dict[str, str]:
    # TODO : construire et retourner les headers
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    return headers


def list_pull_request_files(
    owner: str, repo: str, pull_number: int, token: str
) -> list[dict]:
    # TODO 1 : construire l'URL
    url = build_pr_files_url(owner, repo, pull_number)

    # TODO 2 : construire les headers

    headers = build_headers(token)

    # TODO 3 : effectuer la requête GET
    response = httpx.get(url=url, headers=headers, timeout=10.0)

    # TODO 4 : vérifier le statut HTTP
    response.raise_for_status()

    # TODO 5 : retourner les données JSON
    return response.json()
