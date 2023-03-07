from odoo import models, fields, api , _
from dateutil import relativedelta
from dateutil.relativedelta import relativedelta
from datetime import datetime ,timedelta ,date
class CareCard(models.Model):
    _name = 'care.card'
    card_no = fields.Char(string="Card Number",readonly=True,copy=False,default=lambda self: _('New'),required=True)
    name = fields.Char(string="Beneficiary",required=True)
    issue_date = fields.Date(string='Card Issue Date')
    validity_date =fields.Date(string='Validity Date',readonly=True,compute='_check_change',store=False)
    state = fields.Selection( [('active', 'Active'), ('inactive', 'Inactive'), ('cancel', 'Cancelled')], string='Card State', default='active')
    card_balance = fields.Float(string='Card Balance')
    note = fields.Char(string="Note")


    @api.depends('issue_date')
    def _check_change(self):
        for rec in self:
            if rec.issue_date:
                rec.validity_date=(datetime.strptime(str(rec.issue_date),"%Y-%m-%d")+relativedelta(years=+10))
            else:
                rec.validity_date=False
    # @api.depends('issue_date')
    # def _compute_date(self):
    #     for record in self:
    #         record.validity_date=record.issue_date + datetime.timedelta(years=3)3
    @api.model
    def create(self, vals):

        if not vals.get('note'):
            vals['note'] = ''
        if vals.get('card_no' , _('New')) == _('New'):
            vals['card_no'] = self.env['ir.sequence'].next_by_code('website.module.careCard') or _('New')
        res = super(CareCard, self).create(vals)
        return res
