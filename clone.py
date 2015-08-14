from git_connect import connect
import subprocess


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
        if not subprocess.check_call(['git', 'clone', repo.clone_url]):
            # Returns 0 when ran successfully and 1 otherwise.
            pass
        else:
            print("Clone failed! Try again.")
