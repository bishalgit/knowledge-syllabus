# -*- coding: utf-8 -*-

import logging

from odoo import http, _

_logger = logging.getLogger()


class Share(http.Controller):

    def get_share_qweb_context(self, id, token):
        """
        This function is responsible for either returning the required context of the
        share or render the error message to the portal user.
        """
        try:
            syllabus = http.request.env['document.page'].sudo().search([('id', '=', id)])
        except Exception:
            return http.request.not_found()
        if not syllabus:
            return http.request.not_found()
        if token:
            if token == syllabus.access_token:
                content_status = 'approved'
                content = syllabus.content
                return {
                    'content_status': content_status,
                    'content': content,
                }
        return http.request.not_found()

    @http.route(["/share/syllabus/<int:id>/<token>"], type='http', auth='public')
    def share_syllabus_public(self, id, token, **post):
        share_context = self.get_share_qweb_context(id, token)
        if not isinstance(share_context, dict):
            return share_context

        return http.request.render('syllabus_share.display_syllabus', share_context)
