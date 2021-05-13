#-*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_sending_state = fields.Selection([
        ('not_sent', 'Not sent'),
        ('sent', 'Sent'),
    ], string='Sending state', compute='_compute_invoice_sending_state')

    def _compute_invoice_sending_state(self):
        for record in self:
            record.invoice_sending_state = 'sent' if record.is_move_sent else 'not_sent'