from pathlib import Path


def on_page_markdown(markdown, page, config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    source = Path(page.file.src_path)

    if source == Path("index.md"):
        return markdown

    if source.name == "index.md" and source.parent != Path("."):
        folder = docs_dir / source.parent
        
        folders = []
        for item in sorted(folder.iterdir()):
            if item.name.startswith(".") or item.name == "index.md":
                continue
            if item.is_dir():
                folders.append(item)

        listing = ""

        if folders:
            folder_buttons = []
            for folder_item in sorted(folders):
                name = folder_item.name.replace("-", " ").replace("_", " ").lower()
                folder_buttons.append(
                    f'<a class="subfolder-btn" href="{folder_item.name}/">'
                    f'<span class="folder-icon-box">📁</span>'
                    f'<span class="folder-label">{name}</span>'
                    f'</a>'
                )
            listing += f'\n\n<div class="subfolder-buttons">\n' + "\n".join(folder_buttons) + '\n</div>\n'

        if listing:
            return markdown.rstrip() + listing

    return markdown
