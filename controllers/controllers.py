# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MyPortalController(http.Controller):

    @http.route('/my/admission/online/applications/student', type='http', auth='user', website=True)
    def my_student_route(self, **kw):
        information = http.request.env['se.student'].search([])
        return request.render("smartedu_portal.se_student_template", {
            'info': information,
        })
    
    # @http.route('/my/admission/online/applications/list', type='http', auth='user', website=True)
    # def my_student_admission_route(self, **kw):
    #     applicant_info = http.request.env['se.application'].search([])
    #     return request.render("smartedu_portal.se_student_application_list",{
    #         'informations': applicant_info,
    #     })

    @http.route('/my/admission/online/applications/list/form', type='http', auth='user', website=True)
    def my_student_admission_list_route(self, **kw):
        return request.render("smartedu_portal.se_student_admission_template")

class MyApplicationController(http.Controller):
    @http.route('/my/admission/online/applications/list', type='http', auth='user', website=True)
    def my_student_admission_route(self, **kw):
        applicant_info = http.request.env['se.application'].search([])
        return request.render("smartedu_portal.se_student_application_list", {
            'informations': applicant_info,
        })

# Sending Data From Portal to Backend

class MyApplicationSendingController(http.Controller):
    @http.route('/create/applicant', type='http', auth='user', website=True)
    def create_applicant(self, **kw):
        request.env['se.application'].sudo().create(kw)
        return request.render("smartedu_portal.applicant_thanks")
