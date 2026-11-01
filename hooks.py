from pathlib import Path


def on_page_markdown(markdown, page, config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    source = Path(page.file.src_path)

    # Homepage: list directories
    if source == Path("index.md"):
        cards = []

        for folder in sorted(docs_dir.iterdir()):
            if not folder.is_dir() or not (folder / "index.md").exists():
                continue

            name = folder.name.replace("-", " ").replace("_", " ").title()
            cards.append(
                f'''<a class="directory-card" href="{folder.name}/">
                    <div class="card-top">
                        <span class="folder-icon">▣</span>
                        <h2>{name.lower()}</h2>
                        <span class="card-id">DIRECTORY</span>
                    </div>
                    <span class="card-link">OPEN DIRECTORY →</span>
                </a>'''
            )

        listing = (
            '<div class="directory-grid">\n'
            + "\n".join(cards)
            + "\n</div>"
        )

        return markdown.replace("<!-- AUTO-DIRECTORIES -->", listing)

    # Category overview: list Markdown files
    if source.name == "index.md" and source.parent != Path("."):
        folder = docs_dir / source.parent

        files = sorted(
            file for file in folder.glob("*.md")
            if file.name != "index.md"
        )

        if not files:
            return markdown

        listing = "\n\n## Contents\n\n"

        for file in files:
            title = file.stem.replace("-", " ").replace("_", " ").title()
            listing += f"- [{title}]({file.name})\n"

        return markdown.rstrip() + listing

    return markdown
