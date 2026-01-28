"""
Genera changelog semanal desde commits git y lo agrega a docs/changelog.md
"""

import subprocess
import os

def get_commits():
    result = subprocess.run(
        ["git", "log", "--pretty=format:- %h - %s", "--since=7.days"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def update_changelog(commits):
    changelog_path = "docs/changelog.md"
    if not os.path.exists(changelog_path):
        print("Archivo docs/changelog.md no encontrado.")
        return

    with open(changelog_path, "r") as f:
        content = f.read()

    # Buscar la sección [Unreleased] y agregar commits
    if "## [Unreleased]" in content:
        lines = content.split("\n")
        for i, line in enumerate(lines):
            if line.startswith("## [Unreleased]"):
                # Agregar commits después del header
                insert_index = i + 1
                while insert_index < len(lines) and not lines[insert_index].startswith("## ["):
                    insert_index += 1
                # Insertar commits antes de la siguiente sección
                lines.insert(insert_index, commits)
                break
        new_content = "\n".join(lines)
    else:
        # Si no hay [Unreleased], agregar al final
        new_content = content + "\n## [Unreleased]\n" + commits

    with open(changelog_path, "w") as f:
        f.write(new_content)

    print("Changelog actualizado en docs/changelog.md")

if __name__ == "__main__":
    commits = get_commits()
    if commits:
        print("Commits de la semana:\n", commits)
        update_changelog(commits)
    else:
        print("No hay commits en los últimos 7 días.")