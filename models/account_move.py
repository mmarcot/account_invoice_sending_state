#-*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_sent_state = fields.Selection([
        ('not_sent', 'Not sent'),
        ('sent', 'Sent'),
    ], string='Sending status', compute='_compute_invoice_sent_state')

    def _compute_invoice_sent_state(self):
        for record in self:
            record.invoice_sent_state = 'sent' if record.invoice_sent else 'not_sent'