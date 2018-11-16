# -*- coding: utf-8 -*-
"""
    :author: Guowei
    : 网站数据的api
"""
from flask import jsonify, request, current_app, url_for, g
from flask.views import MethodView

from apis.v1 import api_v1
from apis.v1.auth import generate_token
from apis.v1.errors import api_abort
from apis.v1.schemas import sites_schema, site_schema
from treasure_house.models import Site


class SitesAPI(MethodView):

    def get(self):
        page = request.args.get('page', 1, type=int)
        pagination = Site.query.order_by(Site.timestamp.desc()).paginate(
            page, per_page=current_app.config['TREASURE_HOUSE_MANAGE_POST_PER_PAGE']
        )
        sites = pagination.items
        current = url_for('.sites', page = page, _external=True)
        prev = None
        if pagination.has_prev:
            prev = url_for('.completed_items', page=page - 1, _external=True)
        next = None
        if pagination.has_next:
            next = url_for('.completed_items', page=page + 1, _external=True)
        return jsonify(sites_schema(sites, current, prev, next, pagination))


class SiteAPI(MethodView):

    def get(self,site_id):
        site = Site.query.get_or_404(site_id)
        return jsonify(site_schema(site))


class AuthTokenAPI(MethodView):

    def post(self):
        grant_type = request.form.get('grant_type')
        username = request.form.get('username')
        password = request.form.get('password')

        if grant_type is None or grant_type.lower() != 'password':
            return api_abort(code=400, message='The grant type must be password.')

        # user = User.query.filter_by(username=username).first()
        # if user is None or not user.validate_password(password):
        #     return api_abort(code=400, message='Either the username or password was invalid.')
        #
        # token, expiration = generate_token(user)

        # response = jsonify({
        #     'access_token': token,
        #     'token_type': 'Bearer',
        #     'expires_in': expiration
        # })
        # response.headers['Cache-Control'] = 'no-store'
        # response.headers['Pragma'] = 'no-cache'
        # return response



api_v1.add_url_rule('/website', view_func=SitesAPI.as_view('sites'),
                    methods=['GET'])

api_v1.add_url_rule('/website/<int:site_id>', view_func=SiteAPI.as_view('website'),
                    methods=['GET'])