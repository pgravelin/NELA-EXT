from flask import Markup
from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput, html_params
from wtforms.validators import Required
from models.models import Articles

# Query attribute/field names from the database
field_names = sorted(Articles.__table__.columns.keys())

# Remove dates, since querying by a user input date range requires 
# a reference point
field_names.remove("title1_date")
field_names.remove("title2_date")

# Required for checkbox initialization
field_tuples = [(field_names[4], True)] + [(x, False) for x in field_names[5:-2]]

# Non-digit fields that should be hidden in the sliders form
# We are still loading these into the form for indexing simplicity--possibly refactor?
text_fields = ["normal_display", "lower_display", "sources_display", "title1_date", \
    "title2_date", "title1", "title2", "source1", "source2"]

""" Multiple checkbox form for DB fields """

def select_multi_checkbox(fields, ul_class="", **kwargs):
    kwargs.setdefault("type", "btn")
    html = ["<div class='fields-container' align='left' style='border:2px solid #ccc; width:300px; height: " \
        "400px; overflow-y: scroll;'>"]
    html.append("<ul %s style='list-style-type: none;'>" % html_params(id="fields", class_=ul_class))
    html.append("<div data-toggle='buttons'>")
    for label, checked in fields:
        field_id = "%s" % (label)
        options = dict(kwargs, name=label, id=field_id)
        html.append("<li><label class='btn btn-danger btn-block'>")
        html.append("<input type='checkbox' autocomplete='off' class='invisible field-btn'" \
            "%s>%s</label></li>" % 
                    (html_params(**options), field_id))
    html.append("</div>")
    html.append("</ul>")
    html.append("</div>")
    return "".join(html)

class FieldSelection(FlaskForm):
	Fields = Markup(select_multi_checkbox( fields=field_tuples ) )


""" Multiple slider form for DB field filtering """

def multi_field_sliders(fields, ul_class="", **kwargs):
    kwargs.setdefault("type", "text")
    html = ["<div class='sliders-container' align='center' style='border:2px solid #ccc; width:350px; height: " \
        "375px; overflow-y: scroll;'>"]
    html.append("<ul %s style='list-style-type: none;'>" % (html_params(id="fields", class_=ul_class)))
    for field in fields:
        slider_id = "%s" % (field)
        slider_settings = "data-type='double' data-min='-100' data-max='100' data-from='-100' data-to='100' data-grid='true'"
        options = dict(kwargs, name=field, id=slider_id)
        hidden_option = "hidden" if slider_id in text_fields else ""
        html.append("<li %s><div class='pl-4 pt-5 bd-highlight field-slider' id='%s_container'>" % (hidden_option, slider_id))
        html.append("<input %s class='js-range-slider' %s/> " % (html_params(**options), slider_settings))
        html.append("<label for='%s' class='slider-label'>%s</label></div></li>" % (slider_id, slider_id))
    html.append("</ul>")
    html.append("</div>")
    return "".join(html)

class FieldSliders(FlaskForm):
    Sliders = None

    def __init__(self, fields):
        self.Sliders = Markup(multi_field_sliders (fields=fields) )