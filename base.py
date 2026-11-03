from pathlib import Path


def on_page_markdown(markdown, page, config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    source = Path(page.file.src_path)

    if source == Path("index.md"):
        cards = []

        for folder in sorted(docs_dir.iterdir()):
            if not folder.is_dir() or not (folder / "index.md").exists():
                continue

            name = folder.name.replace("-", " ").replace("_", " ").lower()
            cards.append(
                f'''<a class="directory-card" href="{folder.name}/">
                    <div class="card-top">
                        <span class="folder-icon">▣</span>
                        <h2>{name.lower()}</h2>
                        <span class="card-id">DIRECTORY</span>
                    </div>
                    <span class="card-link">CHECK CATEGORY →</span>
                </a>'''
            )

        listing = (
            '<div class="directory-grid">\n'
            + "\n".join(cards)
            + "\n</div>"
        )

        return markdown.replace("<!-- AUTO-DIRECTORIES -->", listing)

    if source.name == "index.md" and source.parent != Path("."):
        folder = docs_dir / source.parent
        
        files = []
        for item in sorted(folder.iterdir()):
            if item.name.startswith(".") or item.name == "index.md":
                continue
            if item.is_file() and item.suffix == ".md":
                files.append(item)

        files.sort(key=lambda x: x.stat().st_mtime, reverse=True)

        if files:
            file_items = []
            for file_item in files:
                title = file_item.stem.replace("-", " ").replace("_", " ").lower()
                file_items.append(
                    f'<a href="{file_item.stem}/" class="explorer-item">'
                    f'<span class="explorer-icon">📄</span>'
                    f'<span class="explorer-name">{title}</span>'
                    f'</a>'
                )
            listing = f'\n\n<div class="explorer-list">\n' + "\n".join(file_items) + '\n</div>\n'
            return markdown.rstrip() + listing

    return markdown
