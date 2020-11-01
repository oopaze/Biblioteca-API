from flask import Blueprint
import markdown.extensions.fenced_code
from pygments.formatters import HtmlFormatter

formatter = HtmlFormatter(style="emacs",full=True,cssclass="codehilite")
css_string = formatter.get_style_defs()

src = Blueprint('src', __name__)

@src.route('/', methods=['GET'])
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
    md_css_string = "<style>" + css_string + "</style>"
    md_template = md_css_string + md_template_string
    return md_template
