# -*- coding: utf-8 -*-

from odoo import models, fields


class CompensationStatus(models.Model):
    _inherit = "account.analytic.line"
