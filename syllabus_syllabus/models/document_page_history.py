import difflib
from odoo import api, fields, models
from odoo.tools.translate import _


class DocumentPageHistory(models.Model):

    _name = 'document.page.history'
    _inherit = ['document.page.history', 'mail.thread']
    _description = "Syllabus Change History"

    # Groups Involved in Syllabus History
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        syllabus_history = super(DocumentPageHistory, self).create(vals)
        syllabus_history.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return syllabus_history
    
    # This function filters the syllabus history record for the certain syllabus.
    # @api.model
    # def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
    #     domain = (domain or []) + ['|', ('page_id.faculty_id.university_id.name', '=', self.env.user.university_id.name), ('group_ids.users.id', '=', self.env.uid)]
    #     return super(DocumentPageHistory, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)