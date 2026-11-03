from pathlib import Path


def on_page_markdown(markdown, page, config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    source = Path(page.file.src_path)

    if source == Path("index.md"):
        return markdown

    if source.name == "index.md" and source.parent != Path("."):
        folder_title = source.parent.name.replace("-", " ").replace("_", " ").lower()
        page.title = folder_title

    return markdown
