import io

from app import create_app


def build_client():
    app = create_app({"TESTING": True})
    return app.test_client()


def test_home_page_loads():
    client = build_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"mdView" in response.data


def test_upload_markdown_renders_html():
    client = build_client()
    payload = {
        "markdown_file": (io.BytesIO(b"# Hello\n\nThis is **bold**."), "hello.md")
    }
    response = client.post("/", data=payload, content_type="multipart/form-data")

    assert response.status_code == 200
    assert b"<h1" in response.data
    assert b"Hello" in response.data
    assert b"<strong>bold</strong>" in response.data


def test_non_markdown_file_is_rejected():
    client = build_client()
    payload = {
        "markdown_file": (io.BytesIO(b"plain text"), "notes.txt")
    }
    response = client.post("/", data=payload, content_type="multipart/form-data")

    assert response.status_code == 200
    assert b"Only .md files are supported" in response.data


def test_path_markdown_renders_html(tmp_path):
    sample = tmp_path / "sample.md"
    sample.write_text("## Path Source\n\n- one\n- two", encoding="utf-8")

    client = build_client()
    response = client.post("/", data={"markdown_path": str(sample)})

    assert response.status_code == 200
    assert b"Path Source" in response.data
    assert b"<ul>" in response.data
