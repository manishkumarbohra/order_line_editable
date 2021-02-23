# -*- coding: utf-8 -*-
# Copyright 2020 Manish Kumar Bohra <manishbohra1994@gmail.com> or <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_order_line_editable = fields.Boolean('Order Line Editable',
                                               implied_group='order_line_editable.group_order_line_editable')
