# coding=utf-8
from wtforms import Form, StringField, TextAreaField, validators


class NewBlogEntryForm(Form):
    title = StringField('title', [validators.Length(min=4, max=25)])
    content = TextAreaField('content', [validators.Length(min=4, max=250)])

    # submit = StringField('submit')

