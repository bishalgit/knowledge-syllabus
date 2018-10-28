from odoo import api, fields, models


class DocumentPage(models.Model):

    _inherit = 'document.page'
    _description = 'Syllabus'

    course_id = fields.Many2one('syllabus_minister.course',string='Course')
    attachment_id = fields.Many2one('ir.attachment',string='Decision Attachment')
    faculty_id = fields.Many2one('syllabus_minister.faculty',string="Faculty")
    content = fields.Html(
        "Content",
        compute='_compute_content',
        inverse='_inverse_content',
        search='_search_content',
        required=True,
    )

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
    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        domain = (domain or []) + ['|', ('faculty_id.university_id.name', '=', self.env.user.university_id.name), ('group_ids.users.id', '=', self.env.uid)]
        return super(DocumentPage, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit,
                                                     order=order)
