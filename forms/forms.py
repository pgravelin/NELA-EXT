from flask import Markup
from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput, html_params
from wtforms.validators import Required
from models.models import Articles

field_names = Articles.__table__.columns.keys()
field_tuples = [(field_names[4], True)] + [(x, False) for x in field_names[5:-2]]

""" Multiple checkbox form for DB fields """

def select_multi_checkbox(fields, ul_class="", **kwargs):
    kwargs.setdefault("type", "checkbox")
    html = ["<div class='fields-container' align='center' style='border:2px solid #ccc; width:300px; height: " \
        "400px; overflow-y: scroll;'>"]
    html.append("<ul %s style='list-style-type: none;'>" % html_params(id="fields", class_=ul_class))
    for label, checked in fields:
        field_id = "%s" % (label)
        options = dict(kwargs, name=label, id=field_id, class_="btn btn-danger btn-block field-btn")
        html.append("<li><button type='button' data-toggle='button' aria-pressed='false' autocomplete='off' %s>" \
            "%s</button>" % (html_params(**options), field_id))
        html.append("</li>")
    html.append("</ul>")
    html.append("</div>")
    return "".join(html)

class FieldSelection(FlaskForm):
	Fields = Markup(select_multi_checkbox( fields=field_tuples ) )


""" Multiple slider form for DB field filtering """

def multi_field_sliders(fields, ul_class="", **kwargs):
    kwargs.setdefault("type", "text")
    html = ["<div class='sliders-container' align='center' style='border:2px solid #ccc; width:350px; height: " \
        "400px; overflow-y: scroll;'>"]
    html.append("<ul %s style='list-style-type: none;'>" % html_params(id="fields", class_=ul_class))
    for field in fields:
        slider_id = "%s" % (field)
        slider_settings = "data-type='double' data-min='-100' data-max='100' data-from='-100' data-to='100' data-grid='true'"
        options = dict(kwargs, name=field, id=slider_id)
        html.append("<li><div class='pl-4 pt-5 bd-highlight field-slider' id='%s_container'>" % slider_id)
        html.append("<input %s class='js-range-slider' %s/> " % (html_params(**options), slider_settings))
        html.append("<label for='%s' class='slider-label'>%s</label></div></li>" % (slider_id, slider_id))
    html.append("</ul>")
    html.append("</div>")
    return "".join(html)

class FieldSliders(FlaskForm):
    Sliders = None

    def __init__(self, fields):
        self.Sliders = Markup(multi_field_sliders (fields=fields) )