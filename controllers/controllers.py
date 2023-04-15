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
        return request.render("smartedu_portal.se_student_application_list", {
            'informations': applicant_info,
        })

    # @http.route('/my/admission/online/applications/list/form', type='http', auth='user', website=True)
    # def my_student_admission_form_route(self, **kw):
    #     user_id = request.env.context.get('uid')
    #     kw.update({"user_id": user_id})
    #     if request.httprequest.method == 'POST':

    #     # Handle update button click to update data
    #         student_id = int(kw.get('student_id'))
    #         student = request.env['se.application'].sudo().browse(
    #             student_id)
    #         student.update({
    #         'first_name': kw.get('first_name'),
    #         'email': kw.get('email'),
    #         'phone': kw.get('phone'),
    #     })
    #         return http.redirect_with_hash('/my/admission/online/applications/list/form')
    #     else:
    #     # Display form on initial GET request
    #        student_info = request.env['se.application'].search(
    #            [('user_id', '=', request.env.user.id)], limit=1)
    #        return request.render("smartedu_portal.se_student_admission_template", {
    #            'student_info': student_info,
    #        })

    @http.route('/my/admission/online/applications/list/form', auth='public', website=True)
    def update_form(self, **kw):
        student_info = request.env['se.application'].sudo().search([])

        return request.render('smartedu_portal.se_student_admission_template', {
            "student_info": student_info,

        })

    @http.route('/my/admission/online/applications/update', auth='public', website=True)
    def update(self, **kw):
        request.env.context.get('user_id')
        # get professional skill
        student_info = request.env['se.application'].sudo().search([])

        # update student info with new values
        student_info.first_name = kw["first_name"]
        student_info.middle_name = kw["middle_name"]
        student_info.last_name = kw["last_name"]
        # student_info.student_id = kw["student_id", False]
        # student_info.application_serial_number = kw["application_serial_number", False]
        # student_info.application_number = kw["application_number", False]
        # student_info.application_date = kw["application_date", False]
        # student_info.admission_date = kw["admission_date", False]
        # student_info.admission_expire_date = kw["admission_expire_date", False]
        # student_info.batch_id = kw["batch_id", False]
        # student_info.fees = kw["fees", False]
        # student_info.admission_fee = kw["admission_fee", False]
        # student_info.fees_term_id = kw["fees_term_id", False]
        # student_info.order_id = kw["order_id", False]
        # student_info.academic_faculty_id = kw["academic_faculty_id", False]
        # student_info.department_id = kw["department_id", False]
        # student_info.semester_id = kw["semester_id", False]
        # student_info.semester_type_id = kw["semester_type_id", False]
        # student_info.semester_year_string = kw["semester_year_string", False]
        # student_info.form_apply_type = kw["form_apply_type", False]
        # student_info.student_type = kw["student_type", False]
        # student_info.form_apply_type = kw["form_apply_type", False]
        # student_info.education_shift_id = kw["education_shift_id", False]
        # student_info.campus_type = kw["campus_type", False]
        # student_info.registration_number_ssc = kw["registration_number_ssc", False]
        # student_info.roll_number_ssc = kw["roll_number_ssc", False]
        # student_info.education_board_ssc_id = kw["education_board_ssc_id", False]
        # student_info.year_ssc = kw["year_ssc", False]
        # student_info.ssc_gpa = kw["ssc_gpa", False]
        # student_info.ssc_certificate = kw["ssc_certificate", False]
        # student_info.registration_number_hsc = kw["registration_number_hsc", False]
        # student_info.roll_number_hsc = kw["roll_number_hsc", False]
        # student_info.education_board_hsc_id = kw["education_board_hsc_id", False]
        # student_info.year_hsc = kw["year_hsc", False]
        # student_info.hsc_gpa = kw["hsc_gpa", False]
        # student_info.hsc_certificate = kw["hsc_certificate", False]
        # student_info.education_board_o_level_id = kw["education_board_o_level_id", False]
        # student_info.passing_year_o_level = kw["passing_year_o_level", False]
        # student_info.admission_board_result_o_level_ids = kw["admission_board_result_o_level_ids", False]
        # student_info.education_board_a_level_id = kw["education_board_a_level_id", False]
        # student_info.education_board_a_level_id = kw["education_board_a_level_id", False]
        # student_info.passing_year_a_level = kw["passing_year_a_level", False]
        # student_info.admission_board_result_a_level_ids = kw["admission_board_result_a_level_ids", False]
        student_info.gender = kw["gender"]
        # student_info.marital_status = kw["marital_status", False]
        # student_info.religion = kw["religion", False]
        # student_info.blood_group = kw["blood_group", False]
        # student_info.email = kw["email", False]
        # student_info.phone = kw["phone", False]
        # student_info.emergency_contact_info = kw["emergency_contact_info", False]
        # student_info.street = kw["street", False]
        # student_info.zip = kw["zip", False]
        # student_info.permanent_district_id = kw["permanent_district_id", False]
        # student_info.country_id = kw["country_id", False]
        # student_info.present_street = kw["present_street", False]
        # student_info.present_zip = kw["present_zip", False]
        # student_info.present_district_id = kw["present_district_id", False]
        # student_info.present_country_id = kw["present_country_id", False]
        # student_info.is_permanent_present_address_same = kw["is_permanent_present_address_same", False]
        # student_info.whatsapp_number = kw["whatsapp_number", False]
        # student_info.social_network = kw["social_network", False]
        # student_info.nationality = kw["nationality", False]
        # student_info.national_id_no = kw["national_id_no", False]
        # student_info.passport_no = kw["passport_no", False]
        # student_info.visa_no = kw["visa_no", False]
        # student_info.nationalID = kw["nationalID", False]
        # student_info.visa_no = kw["visa_no", False]
        # student_info.visa_expire_date = kw["visa_expire_date", False]
        # student_info.father_name = kw["father_name", False]
        # student_info.father_contact_number = kw["father_contact_number", False]
        # student_info.father_email = kw["father_email", False]
        # student_info.father_national_id = kw["father_national_id", False]
        # student_info.father_passport = kw["father_passport", False]
        # student_info.father_birthday = kw["father_birthday", False]
        # student_info.father_age = kw["father_age", False]
        # student_info.father_occupation = kw["father_occupation", False]
        # student_info.father_designation = kw["father_designation", False]
        # student_info.father_annual_income = kw["father_annual_income", False]
        # student_info.mother_name = kw["mother_name", False]
        # student_info.mother_contact_number = kw["mother_contact_number", False]
        # student_info.mother_email = kw["mother_email", False]
        # student_info.mother_national_id = kw["mother_national_id", False]
        # student_info.mother_passport = kw["mother_passport", False]
        # student_info.mother_birthday = kw["mother_birthday", False]
        # student_info.mother_age = kw["mother_age", False]
        # student_info.mother_occupation = kw["mother_occupation", False]
        # student_info.mother_designation = kw["mother_designation", False]
        # student_info.local_guardian_name = kw["local_guardian_name", False]
        # student_info.local_guardian_email = kw["local_guardian_email", False]
        # student_info.local_guardian_contact_number = kw["local_guardian_contact_number", False]
        # student_info.local_guardian_national_id = kw["local_guardian_national_id", False]
        # student_info.local_guardian_passport = kw["local_guardian_passport", False]
        # student_info.local_guardian_relation = kw["local_guardian_relation", False]
        # student_info.local_guardian_street = kw["local_guardian_street", False]
        # student_info.local_guardian_zip = kw["local_guardian_zip", False]
        # student_info.local_guardian_state_id = kw["local_guardian_state_id", False]
        # student_info.local_guardian_country_id = kw["local_guardian_country_id", False]
       


        return request.redirect('/my/admission/online/applications/list')


    # @http.route('/my/admission/online/applications/list/form', type='http', auth='user', website=True)
    # def my_student_admission_list_route(self, **kw):
    #     user_id = request.env.context.get('uid')
    #     kw.update({"user_id": user_id})
    #     if request.httprequest.method == 'POST':
    #     # Handle POST request to update data
    #         student = request.env['se.application'].sudo().browse(user_id)
    #         student.update(kw)
    #         return http.redirect_with_hash('/my/admission/online/applications/list/form')
    #     else:
    #     # Handle GET request to display form
    #         student_info = http.request.env['se.application'].search([])
    #         return request.render("smartedu_portal.se_student_admission_template", {
    #         'student_info': student_info,
    #     })



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
