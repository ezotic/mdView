import bleach
import markdown as markdown_lib

ALLOWED_TAGS = set(bleach.sanitizer.ALLOWED_TAGS).union(
    {
        "p",
        "pre",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "hr",
        "span",
        "table",
        "thead",
        "tbody",
        "tr",
        "th",
        "td",
        "code",
        "blockquote",
        "img",
    }
)

ALLOWED_ATTRIBUTES = {
    **bleach.sanitizer.ALLOWED_ATTRIBUTES,
    "a": ["href", "title", "target", "rel"],
    "img": ["src", "alt", "title"],
    "th": ["align"],
    "td": ["align"],
    "code": ["class"],
    "span": ["class"],
}


def render_markdown(markdown_text: str) -> str:
    rendered_html = markdown_lib.markdown(
        markdown_text,
        extensions=[
            "extra",
            "fenced_code",
            "tables",
            "toc",
            "sane_lists",
            "codehilite",
        ],
        output_format="html5",
    )

    return bleach.clean(
        rendered_html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        protocols=["http", "https", "mailto"],
        strip=True,
    )
