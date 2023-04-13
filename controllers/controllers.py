# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import base64
import logging
import json


class MyPortalController(http.Controller):


    @http.route('/my/admission/online/applications/student', type='http', auth='user', website=True)
    def my_student_route(self, **kw):
        information = http.request.env['se.student'].search([])
        return request.render("smartedu_portal.se_student_template", {
            'info': information,
        })
    
    @http.route('/my/admission/online/applications/list', type='http', auth='user', website=True)
    def my_student_admission_route(self, **kw):
        applicant_info = http.request.env['se.application'].search([])
        return request.render("smartedu_portal.se_student_application_list",{
            'informations': applicant_info,
        })
    
    @http.route('/my/admission/online/applications/list/form', type='http', auth='user', website=True)
    def my_student_admission_form_route(self, **kw):
        if request.httprequest.method == 'POST':
            if 'view' in kw:
            # Handle view button click to display data
                student_info = request.env['se.application'].search([])
                return request.render("smartedu_portal.se_student_admission_template", {
                'student_info': student_info,
            })
            elif 'update' in kw:
            # Handle update button click to update data
                student_id = int(kw.get('student_id'))
                student = request.env['se.application'].sudo().browse(student_id)
                student.update(kw)
                return http.redirect_with_hash('/my/admission/online/applications/list/form')
        else:
        # Display form on initial GET request
            student_info = request.env['se.application'].search([])
            return request.render("smartedu_portal.se_student_admission_template", {
            'student_info': student_info,
        })




    # @http.route('/my/admission/online/applications/list/form', type='http', auth='user', website=True)
    # def my_student_admission_list_route(self, **kw):
    #     if request.httprequest.method == 'POST':
    #     # Handle POST request to update data
    #         student_id = int(kw.get('student_id'))
    #         student = request.env['se.application'].sudo().browse(student_id)
    #         student.update(kw)
    #         return http.redirect_with_hash('/my/admission/online/applications/list/form')
    #     else:
    #     # Handle GET request to display form
    #         student_info = http.request.env['se.application'].search([])
    #         return request.render("smartedu_portal.se_student_admission_template", {
    #         'student_info': student_info,
    #     })
        # return request.render("smartedu_portal.se_student_admission_template")


# Update 

# @http.route('/my/admission/online/applications/list/form', type='http', auth='user', website=True)
# def my_student_admission_form_route(self, **kw):
#     if request.httprequest.method == 'POST':
#         # Handle POST request to update data
#         student_id = int(kw.get('student_id'))
#         student = request.env['se.application'].sudo().browse(student_id)
#         student.update(kw)
#         return http.redirect_with_hash('/my/admission/online/applications/list/form')
#     else:
#         # Handle GET request to display form
#         student_info = request.env['se.application'].search([])
#         return request.render("smartedu_portal.se_student_admission_template", {
#             'student_info': student_info,
#         })


# Create Data From Portal to Backend

    # @http.route('/create/applicant', type='http', auth='user', website=True)
    # def create_applicant(self, **kw):

    #     # set current user
    #     user_id = request.env.context.get('uid')
    #     kw.update({"user_id": user_id})

    #     # set student  id
    #     request.env['se.application'].sudo().search(
    #         [('user_id', '=', user_id)], limit=1)

    #     request.env['se.application'].sudo().create(kw)
    #     return request.render("smartedu_portal.applicant_thanks", {})
