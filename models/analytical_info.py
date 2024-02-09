# -*- coding: utf-8 -*-

from odoo import models, fields, api

class analytical_info(models.Model):
  _name "info.analytical_info"

  project = fields.Char(string='Project',required=True)
  source = fields.Char(string='Source'required=True)
  source_type = fields.Char(string='Source type'required=True)
  value = fields.Integer(string='Value',required=True,default=0)
