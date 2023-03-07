# -*- coding: utf-8 -*-
from odoo import http

class Academy(http.Controller):

    @http.route('/my/page/', auth='public', website=True)
    def index(self, **kw):
        Beneficiary = http.request.env['care.card']
        return http.request.render('website-module.index', {
            'bf': Beneficiary.search([])
        # return http.request.render('website-module.index', {
        #     'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })