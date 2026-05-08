from pathlib import Path

from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

from .markdown_utils import render_markdown

bp = Blueprint("main", __name__)


def _read_uploaded_file():
    file_obj = request.files.get("markdown_file")
    if not file_obj or file_obj.filename == "":
        return None, None

    filename = secure_filename(file_obj.filename)
    if not filename.lower().endswith(".md"):
        raise ValueError("Only .md files are supported.")

    data = file_obj.read()
    text = data.decode("utf-8")
    return filename, text


def _read_markdown_path(raw_path: str):
    if not raw_path:
        return None, None

    candidate = Path(raw_path).expanduser().resolve()
    if candidate.suffix.lower() != ".md":
        raise ValueError("Path must point to a .md file.")
    if not candidate.exists() or not candidate.is_file():
        raise ValueError("File path does not exist.")

    text = candidate.read_text(encoding="utf-8")
    return str(candidate), text


@bp.route("/", methods=["GET", "POST"])
def index():
    rendered_html = ""
    error = ""
    source_name = ""

    if request.method == "POST":
        path_input = request.form.get("markdown_path", "").strip()

        try:
            source_name, markdown_text = _read_uploaded_file()
            if markdown_text is None:
                source_name, markdown_text = _read_markdown_path(path_input)

            if markdown_text is None:
                raise ValueError("Choose a .md file or enter a valid .md path.")

            rendered_html = render_markdown(markdown_text)
        except UnicodeDecodeError:
            error = "File must be UTF-8 encoded."
        except OSError:
            error = "Could not read the selected file."
        except ValueError as exc:
            error = str(exc)

    return render_template(
        "index.html",
        rendered_html=rendered_html,
        error=error,
        source_name=source_name,
    )
