from odoo import http
from odoo.http import request
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class CreateFromFormController(http.Controller):
    @http.route('/create_from_web', type='http', auth='public', website=True)
    def create_form(self, **kwargs):
        partners = request.env['res.partner'].sudo().search([])
        return request.render('create_from_form_web.create_form_template', {
            'partners': partners
        })

    @http.route('/submit_form_web', type='http', auth='public', methods=['POST'], website=True)
    def submit_form_web(self, **post):
        model = request.env['model_all_types'].sudo()
        form_data = request.httprequest.form
        files = request.httprequest.files

        model.create_from_web(form_data, files)
          
        return request.redirect('/create_from_web')