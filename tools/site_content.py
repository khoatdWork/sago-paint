"""Read the same public page inventory as the build; no files are changed."""
import json
import subprocess
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def inventory():
    return json.loads(subprocess.check_output(["node", str(ROOT / "tools/site-files.js")], cwd=ROOT, text=True, encoding="utf-8"))


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.meta, self.links, self.assets, self.ids = {}, [], [], set()
        self.canonicals, self.headings, self.schemas, self.images, self.styles = [], [], [], [], []
        self.title, self.lang, self.h1_count = "", "", 0
        self._heading, self._title, self._schema = None, False, None
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "br" and self._heading:
            self._heading[1] += " "
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang", "")
        if tag == "title":
            self._title = True
        if tag in ("h1", "h2", "h3"):
            self._heading = [tag, ""]
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta":
            self.meta[a.get("name", a.get("property", ""))] = a.get("content", "")
        if tag == "a":
            self.links.append(a.get("href", ""))
        if tag == "link":
            if a.get("rel") == "canonical":
                self.canonicals.append(a.get("href", ""))
            if a.get("rel") == "stylesheet":
                self.styles.append(a.get("href", ""))
                self.assets.append(a.get("href", ""))
        if tag in ("img", "script") and a.get("src"):
            self.assets.append(a["src"])
        if tag == "img":
            self.images.append(a)
        if tag == "script" and a.get("type") == "application/ld+json":
            self._schema = ""

    def handle_endtag(self, tag):
        if tag == "title":
            self._title = False
        if self._heading and tag == self._heading[0]:
            self.headings.append(tuple(self._heading))
            self._heading = None
        if tag == "script" and self._schema is not None:
            self.schemas.append(json.loads(self._schema))
            self._schema = None

    def handle_data(self, data):
        if self._title:
            self.title += data
        if self._heading:
            self._heading[1] += data
        if self._schema is not None:
            self._schema += data


def schema_types(value):
    if isinstance(value, list):
        return set().union(*(schema_types(item) for item in value)) if value else set()
    if not isinstance(value, dict):
        return set()
    types = value.get("@type", [])
    return set(types if isinstance(types, list) else [types]) | schema_types(value.get("@graph", []))


def context_path(route):
    return ROOT / "docs/pages" / (route.strip("/") or "home") / "CONTEXT.md"
