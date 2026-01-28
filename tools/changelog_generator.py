"""
Genera changelog semanal desde commits git
"""

import subprocess

def get_commits():
    result = subprocess.run(
        ["git", "log", "--pretty=format:%h - %s", "--since=7.days"],
        capture_output=True,
        text=True
    )
    return result.stdout

if __name__ == "__main__":
    commits = get_commits()
    print("Weekly changelog:\n", commits)
    with open("CHANGELOG_WEEKLY.md", "w") as f:
        f.write("# Weekly Changelog\n\n")
        f.write(commits)