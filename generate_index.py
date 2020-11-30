from jinja2 import Environment, FileSystemLoader
import os
from pathlib import Path
HTML_NOTEBOOK_ROOT = os.environ.get('HTML_NOTEBOOK_ROOT', 'public')
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html.template')

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


notebook_root = Path(HTML_NOTEBOOK_ROOT)
days = [x for x in notebook_root.iterdir()]
html_urls = []
for (idx, day) in enumerate(sorted(days)):
    html_urls.append((idx + 1, [remove_prefix(str(x), 'public/') for x in day.iterdir()][0]))
# Get all the html_notebooks
days_remaining = list(range(len(html_urls) + 1, 26))
rendered_html = template.render(notebook_urls=sorted(html_urls), days_remaining=days_remaining)

with open("public/index.html", "w") as fh:
    fh.write(rendered_html)