# -*- coding: utf-8 -*-
"""
    :author: Guowei
"""
from flask import Blueprint, render_template, flash, url_for
from flask_login import login_required
from werkzeug.utils import redirect

from treasure_house.extensions import db
from treasure_house.forms import SiteForm
from treasure_house.models import Site, Category

sites_bp = Blueprint('sites', __name__)


@sites_bp.route('/sites')
def index():
    sites = Site.query.order_by(Site.timestamp.desc()).all()
    return render_template('sites/index.html', sites=sites)


@sites_bp.route('/site/new', methods=['GET', 'POST'])
@login_required
def new_site():
    form = SiteForm()
    if form.validate_on_submit():
        name = form.name.data
        url = form.url.data
        description = form.description.data
        category = Category.query.get(form.category.data)
        link = Site(name=name, url=url, category=category, description=description)
        db.session.add(link)
        db.session.commit()
        flash('Site created.', 'success')
        return redirect(url_for('.index'))
    return render_template('sites/new_site.html', form=form)
