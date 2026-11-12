# Usage: python render_html.py METADATA_TEMPLATE
import re
import sys
from pathlib import Path

import yaml
import jinja2

DATASETS_DIR = Path(__file__).parent.parent / "datasets"


def replace_links(text):
    """Replaces [link text](url) with HTML <a> tags."""
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)


JINJA_ENV = jinja2.Environment()
JINJA_ENV.filters["replace_links"] = replace_links

HTML_TEMPLATE_STR = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{ data.Name }}</title>
        <style>
            body { font-family: sans-serif; display: flex; }
            .left-column { width: 60%; padding-right: 20px; }
            .right-column { width: 40%; padding-left: 20px; border-left: 1px solid #eee; }
            .section { margin-bottom: 20px; }
            .section h2 { border-bottom: 1px solid #ccc; padding-bottom: 5px; }
            .resource { border: 1px solid #eee; padding: 10px; margin-bottom: 10px; }
            .tutorial { border: 1px solid #eee; padding: 10px; margin-bottom: 10px; }
        </style>
    </head>
    <body>
        <div class="left-column">
            <h1>{{ data.Name }}</h1>
            <div class="section">
                <p>
                    {% for tag in data.Tags %}
                        [ {{ tag }} ]{% if not loop.last %}{% endif %}
                    {% endfor %}
                </p>
            </div>
            <div class="section">
                <h2>Description</h2>
                <p>{{ data.Description | replace_links | safe }}</p>
            </div>
            <div class="section">
                <h3>Update Frequency</h3>
                <p>{{ data.UpdateFrequency }}</p>
            </div>
            <div class="section">
                <h3>License</h3>
                <p><a href="{{ data.License }}">{{ data.License }}</a></p>
            </div>
            <div class="section">
                <h3>Documentation</h3>
                <p><a href="{{ data.Documentation }}">{{ data.Documentation }}</a></p>
            </div>
            <div class="section">
                <h3>Managed By</h3>
                <p>{{ data.ManagedBy | replace_links | safe }}</p>
            </div>
            <div class="section">
                <h3>Contact</h3>
                <p><a href="{{ data.Contact }}">{{ data.Contact }}</a></p>
            </div>
            <div class="section">
                <h3>How to Cite</h3>
                <p>{{ data.Citation | replace_links | safe }}</p>
            </div>
            <div class="section">
                <h3>Usage Examples</h3>
                <p>Tutorials</p>
                {% for tutorial in data.DataAtWork.Tutorials %}
                <div class="tutorial">
                    <p><a href="{{ tutorial.URL }}">{{ tutorial.Title }}</a></h4>
                    by <a href="{{ tutorial.AuthorURL }}">{{ tutorial.AuthorName }}</a></p>
                </div>
                {% endfor %}
            </div>
        </div>
        <div class="right-column">
            <div class="section">
                <h2>Resources on AWS</h2>
                {% for resource in data.Resources %}
                <div class="resource">
                    <p>Description<br>{{ resource.Description | replace_links | safe }}</p>
                    <p>Resource Type<br>{{ resource.Type }}</p>
                    <p>ARN<br>{{ resource.ARN }}</p>
                    <p>Region<br>{{ resource.Region }}</p>
                    <p>Requester Pays; Account Required
                    <br>{{ resource.RequesterPays }}; {{ resource.AccountRequired }}</p>
                </div>
                {% endfor %}
            </div>
        </div>
    </body>
    </html>
    """


def generate_html(dataset_name):
    fyaml = DATASETS_DIR / f"{dataset_name}.yaml"
    fhtml = DATASETS_DIR / f"{dataset_name}.html"

    with open(fyaml, "r") as f:
        yaml_data = f.read()

    data = yaml.safe_load(yaml_data)
    template = JINJA_ENV.from_string(HTML_TEMPLATE_STR)
    html_output = template.render(data=data)

    with open(fhtml, "w") as f:
        f.write(html_output)

    print(f"HTML file generated: {fhtml}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python render_html.py <dataset_name>")
    else:
        dataset_name = sys.argv[1]
        generate_html(dataset_name)
