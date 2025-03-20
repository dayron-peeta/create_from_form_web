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
        file_content = post.get('binary_field')
       
        request.env['model_all_types'].sudo().create({
            'name': post.get('name'),
            'description': post.get('description'),
            'integer_field': int(post.get('integer_field', 0)),
            'float_field': float(post.get('float_field', 0.0)),
            'boolean_field': bool(post.get('boolean_field')),
            'selection_field': post.get('selection_field'),
            'date_field': post.get('date_field'), 
            'datetime_field': datetime.strptime(post['datetime_field'], '%Y-%m-%dT%H:%M') if post.get('datetime_field', False) else False, # corregir el formato de fecha
            'many2one_field': int(post.get('many2one_field', 0)) if post.get('many2one_field') else False,
            'many2many_field': [(6, 0, [int(id) for id in request.httprequest.form.getlist('many2many_field') if id])], # Obtener valores del campo many2many_field (cadena separada por comas), convertirlos a enteros y eliminar valores vacíos
            'binary_field': file_content.read() if file_content else False
            
        })
        return request.redirect('/create_from_web')