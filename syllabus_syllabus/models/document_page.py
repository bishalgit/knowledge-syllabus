from odoo import api, fields, models, _

import logging

_logger = logging.getLogger(__name__)


class DocumentPage(models.Model):

    _inherit = 'document.page'
    _description = 'Syllabus'

    course_id = fields.Many2one('syllabus_minister.course',string='Course')
    # attachment_ids = fields.Many2many('ir.attachment',string='Decision Attachment')
    faculty_id = fields.Many2one('syllabus_minister.faculty',string="Faculty")
    major_version = fields.Char('Major Version')
    content = fields.Html(
        "Content",
        compute='_compute_content',
        inverse='_inverse_content',
        search='_search_content',
        required=True,
    )
    # no-op computed field
    summary = fields.Text(
        help='Describe the changes made',
        compute=lambda x: x,
        inverse=lambda x: x,
    )

    # Decision date and documents
    decision_date = fields.Date('Decision Date')
    doc_count = fields.Integer(compute='_compute_attached_docs_count', string="Number of documents attached")
    def _compute_attached_docs_count(self):
        Attachment = self.env['ir.attachment']
        for page in self:
            page.doc_count = Attachment.search_count([
                '|', ('res_model', '=', 'document.page'), ('res_id', '=', page.id)
            ])

    @api.multi
    def attachment_tree_view(self):
        self.ensure_one()
        domain = [
            '|', ('res_model', '=', 'document.page'), ('res_id', 'in', self.ids)]
        return {
            'name': _('Decision Attachments'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                        These are the documents of the decision attachments during syllabus
                        management.
                    </p>'''),
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        }

    @api.multi
    def history_tree_view(self):
        self.ensure_one()
        domain = [('page_id', '=', self.id)]
        return {
            'name': _('History'),
            'domain': domain,
            'res_model': 'document.page.history',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'view_type': 'form',
            # 'help': _('''<p class="oe_view_nocontent_create">
            #             These are the documents of the decision attachments during syllabus
            #             management.
            #         </p>'''),
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d, 'create': False, 'edit': False, 'delete': False}" % (self._name, self.id)
        }

    # Groups Involved in Syllabus
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        syllabus = super(DocumentPage, self).create(vals)
        syllabus.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return syllabus

    # Overriding _inverse_content to transfer decision date and attachment in the 
    # syllabus history
    @api.multi
    def _inverse_content(self):
        for rec in self:
            if rec.type == 'content':
                rec.latest_version += 1
                rec._create_history({
                    'content': rec.content,
                    'summary': rec.summary,
                    'decision_date': rec.decision_date,
                    'syllabus_version': rec.latest_version,
                    'final_draft': rec.major_change,
                    'major_version': rec.major_version,
                    'course_id': rec.course_id.id,
                })

    # providing sql contraint for unqiue name of the syllabus objects
    _sql_constraints = [
        ('name_key', 'unique (name)', 'This name already exists, please provide another name for the syllabus.'),
    ]

    # latest version of the syllabus
    latest_version = fields.Integer("Latest Version", default=0)

    # if the change from the syllabus template model is major change
    major_change = fields.Boolean("Major Change", default=False)

    # check if the syllabus required watermark logo of the university
    require_watermark = fields.Boolean("Require Watermark of the University?", default=False)

    @api.multi
    def write(self, vals):
        syllabus = super(DocumentPage, self).write(vals)
        universities = self.env['res.company'].search([])
        if "require_watermark" in vals:
            for university in universities:
                university.write({
                    'require_watermark': vals['require_watermark']
                })
        else:
            for university in universities:
                university.write({
                    'require_watermark': self.require_watermark
                })
        return syllabus
