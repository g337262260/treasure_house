# -*- coding: utf-8 -*-
"""
    :author: Guowei
"""
from flask import url_for


def site_schema(site):
    return {
        'id': site.id,
        'name':site.name,
        'url':site.url
    }


def sites_schema(sites, current, prev, next, pagination):
    return {
        'self': current,
        'kind': 'site',
        'sites': [site_schema(site) for site in sites],
        'prev': prev,
        'last': url_for('.sites', page=pagination.pages, _external=True),
        'first': url_for('.sites', page=1, _external=True),
        'next': next,
        'count': pagination.total
    }
