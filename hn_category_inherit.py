# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HnCategoryInherit(models.Model):
    _inherit = "product.category"

    energy_consumption = fields.Boolean(string="Consumo de Energia", tracking=True)