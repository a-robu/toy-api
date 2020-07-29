#!/usr/bin/env python

import json
import os.path
from flask import Flask, render_template, redirect, url_for, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('page', location='landing'))

@app.route('/api/page/<location>')
def page(location):
    # FIXME consider whether processing user input in this way is unsafe.
    # TODO the pre tags are here only because this is a stub
    chosen_template = os.path.join('pages', '{}.json'.format(location))
    # return '<pre>{}</pre>'.format(
    return jsonify(json.loads(render_template(
        chosen_template,
        alternatives=dict(
            allow_no=request.args.get("allow_no")
        ), answers=dict(
            is_on_vacation=request.args.get("is_on_vacation")
        )
    )))