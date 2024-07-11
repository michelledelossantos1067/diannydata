# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sld_data(models.Model):
    _name = 'sld_data.sld_data'
    _description = 'sld_data.sld_data'

    nombre = fields.Char(string='Nombre')
    apellido = fields.Char(string='Apellido')
    correo = fields.Char(string='Email')
    direccion = fields.Char(string='Dirección')
