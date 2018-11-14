# -*- coding: utf-8 -*-
"""
    :author: Guowei
"""
from flask import Blueprint, render_template, flash, url_for, request, current_app
from flask_login import login_required
from werkzeug.utils import redirect

from treasure_house.extensions import db
from treasure_house.forms import SiteForm, LinkForm
from treasure_house.models import Site, Category, Link

sites_bp = Blueprint('sites', __name__)


@sites_bp.route('/sites')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Site.query.order_by(Site.timestamp.desc()).paginate(
        page, per_page=current_app.config['TREASURE_HOUSE_MANAGE_POST_PER_PAGE']
    )
    sites = pagination.items
    categories = Category.query.filter(Category.id != 1)
    return render_template('sites/index.html', page=page, pagination=pagination, sites=sites, categories=categories)


@sites_bp.route('/site/new', methods=['GET', 'POST'])
@login_required
def new_site():
    form = SiteForm()
    if form.validate_on_submit():
        name = form.name.data
        url = form.url.data
        description = form.description.data
        category = Category.query.get(form.category.data)
        site = Site(name=name, url=url, category=category, description=description)
        db.session.add(site)
        db.session.commit()
        flash('Site created.', 'success')
        return redirect(url_for('.index'))
    return render_template('sites/new_site.html', form=form)


@sites_bp.route('/site/classify')
def classify_site():
    filter_rule = request.args.get('filter', 0, type=int)
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['TREASURE_HOUSE_COMMENT_PER_PAGE']
    if filter_rule == 0:
        filtered_sites = Site.query
    else:
        filtered_sites = Site.query.filter_by(category_id=filter_rule)

    pagination = filtered_sites.order_by(Site.timestamp.desc()).paginate(
        page, per_page=per_page
    )
    sites = pagination.items
    categories = Category.query.filter(Category.id != 1)
    return render_template('sites/index.html', page=page, pagination=pagination,
                           sites=sites, categories=categories, filter_rule=filter_rule)
