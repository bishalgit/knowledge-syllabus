import difflib
from odoo import api, fields, models
from odoo.tools.translate import _

import logging

_logger = logging.getLogger(__name__)


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
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)],
        })
        return syllabus_history

    
    # change requests and approval decision date and attachments
    decision_date = fields.Date('Decision Date')
    doc_count = fields.Integer(compute='_compute_attached_docs_count', string="Number of documents attached")
    def _compute_attached_docs_count(self):
        Attachment = self.env['ir.attachment']
        for page in self:
            page.doc_count = Attachment.search_count([
                '|', ('res_model', '=', 'document.page.history'), ('res_id', '=', page.id)
            ])

    @api.multi
    def attachment_tree_view(self):
        self.ensure_one()
        domain = [
            '|', ('res_model', '=', 'document.page.history'), ('res_id', 'in', self.ids)]
        return {
            'name': _('Change Requests Decision Attachments'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                        These are the documents of the decision attachments during syllabus
                        change request and approval process.
                    </p>'''),
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        }

    # syllabus version field
    syllabus_version = fields.Integer("Version", default=0)

    # compute name for syllabus history with version convention
    name = fields.Char("Name", compute="_compute_name")

    @api.multi
    @api.depends('page_id', 'syllabus_version')
    def _compute_name(self):
        "Compute name for syllabus with version"
        for rec in self:
            rec.name = str(rec.page_id.name) + "_version_" + str(rec.syllabus_version)

    # overriding content field to type HTML
    content = fields.Html('Content')

    # displaying default name field
    @api.multi
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, rec.name))
        return res

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        records = self.search(args, limit=limit)
        if records:
            return self.browse(records.ids).name_get()
        else:
            return []
