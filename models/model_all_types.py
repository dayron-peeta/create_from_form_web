# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

class ModelAllTypes(models.Model):
    _name = 'model_all_types'
    _description = 'Model with All Data Types'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    integer_field = fields.Integer(string='Integer Field')
    float_field = fields.Float(string='Float Field')
    boolean_field = fields.Boolean(string='Boolean Field')
    selection_field = fields.Selection([
        ('option_1', 'Option 1'),
        ('option_2', 'Option 2'),
        ('option_3', 'Option 3')
    ], string='Selection Field')
    date_field = fields.Date(string='Date Field')
    datetime_field = fields.Datetime(string='Datetime Field')
    many2one_field = fields.Many2one('res.partner', string='Many2one Field')
    many2many_field = fields.Many2many('res.partner', string='Many2many Field')
    binary_field = fields.Binary(string='Binary Field')
    
    @api.model
    def create_from_web(self, values):
        """ Crea un registro desde el formulario web """
        return self.create({
            'name': values.get('name'),
            'description': values.get('description'),
            'integer_field': int(values.get('integer_field', 0)),
            'float_field': float(values.get('float_field', 0.0)),
            'boolean_field': bool(values.get('boolean_field')),
            'selection_field': values.get('selection_field'),
            'date_field': values.get('date_field'),
            'datetime_field': datetime.strptime(values['datetime_field'], '%Y-%m-%dT%H:%M') if values.get('datetime_field') else False,
            'many2one_field': int(values.get('many2one_field', 0)) if values.get('many2one_field') else False,
            'many2many_field': [(6, 0, [int(id) for id in values.getlist('many2many_field') if id])],
            'binary_field': values.get('binary_field').read() if values.get('binary_field') else False
        })