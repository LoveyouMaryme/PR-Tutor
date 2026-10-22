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
