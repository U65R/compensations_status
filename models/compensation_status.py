# -*- coding: utf-8 -*-

from odoo import models, fields


class CompensationStatus(models.Model):
    _inherit = "account.analytic.line"


    to_check = fields.Boolean(string="To check", copy=False)
