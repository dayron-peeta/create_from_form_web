# -*- coding: utf-8 -*-
from odoo import models, fields

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