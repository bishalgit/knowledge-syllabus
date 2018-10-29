from odoo import api, fields, models, _


class DocumentPage(models.Model):

    _inherit = 'document.page'
    _description = 'Syllabus'

    course_id = fields.Many2one('syllabus_minister.course',string='Course')
    # attachment_ids = fields.Many2many('ir.attachment',string='Decision Attachment')
    faculty_id = fields.Many2one('syllabus_minister.faculty',string="Faculty")
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

    # Groups Involved in Syllabus
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        syllabus = super(DocumentPage, self).create(vals)
        syllabus.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return syllabus

    # This function filters the syllabus record for the user of certain course.
    # @api.model
    # def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
    #     domain = (domain or []) + ['|', ('faculty_id.university_id.name', '=', self.env.user.university_id.name), ('group_ids.users.id', '=', self.env.uid)]
    #     return super(DocumentPage, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit,
    #                                                  order=order)
