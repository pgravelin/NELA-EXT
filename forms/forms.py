from flask import Markup
from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput, html_params
from wtforms.validators import Required
from models.models import Articles

field_names = Articles.__table__.columns.keys()
field_tuples = [(field_names[4], True)] + [(x, False) for x in field_names[5:-2]]

def select_multi_checkbox(fields, ul_class="", **kwargs):
    kwargs.setdefault("type", "checkbox")
    html = ["<div class='fields-container' align='left' style='border:2px solid #ccc; width:300px; height: " \
        "400px; overflow-y: scroll;'>"]
    html.append("<ul %s style='list-style-type: none;'>" % html_params(id="fields", class_=ul_class))
    for label, checked in fields:
        field_id = "%s" % (label)
        options = dict(kwargs, name=label, id=field_id)
        if checked:
            options["checked"] = "checked"
        html.append("<li><input %s /> " % html_params(**options))
        html.append("<label for='%s'>%s</label></li>" % (field_id, label))
    html.append("</ul>")
    html.append("</div>")
    html.append("</div>")
    return "".join(html)

class FieldSelection(FlaskForm):
	Fields = Markup(select_multi_checkbox( fields=field_tuples ) )


""" TODO: add another form for ranges/sliders """