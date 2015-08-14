from git_connect import connect
import os


def getRepos():
    """Returns all the repos under the user."""
    github = connect()
    user = github.get_user()
    # Get all Repos!
    all_repos = user.get_repos()
    return all_repos


if __name__ == '__main__':
    all_repos = getRepos()
    for repo in all_repos:
        # Clone the repo.
        os.system('git clone ' + repo.clone_url)
    print("Cloned all your Repos.")
