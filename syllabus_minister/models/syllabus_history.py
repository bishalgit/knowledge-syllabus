import difflib
from odoo import api, fields, models
from odoo.tools.translate import _

class SyllabusHistory(models.Model):
    _name = 'syllabus_minister.syllabus_history'
    _inherit = 'mail.thread'
    _order = 'id DESC'

    syllabus_id = fields.Many2one('syllabus_minister.syllabus', 'Syllabus', ondelete='cascade')
    summary = fields.Char('Summary', index=True)
    content = fields.Text("Content")
    diff = fields.Text(compute='_compute_diff')

    @api.multi
    @api.depends('content', 'syllabus_id.history_ids')
    def _compute_diff(self):
        """Shows a diff between this version and the previous version"""
        history = self.env['syllabus_minister.syllabus_history']
        for rec in self:
            prev = history.search([
                ('syllabus_id', '=', rec.syllabus_id.id),
                ('create_date', '<', rec.create_date)],
                limit=1,
                order='create_date DESC')
            if prev:
                rec.diff = self.getDiff(prev.id, rec.id)
            else:
                rec.diff = self.getDiff(False, rec.id)

    @api.model
    def getDiff(self, v1, v2):
        """Return the difference between two version of document version."""
        text1 = v1 and self.browse(v1).content or ''
        text2 = v2 and self.browse(v2).content or ''
        # Include line breaks to make it more readable
        # TODO: consider using a beautify library directly on the content
        text1 = text1.replace('</p><p>', '</p>\r\n<p>')
        text2 = text2.replace('</p><p>', '</p>\r\n<p>')
        line1 = text1.splitlines(1)
        line2 = text2.splitlines(1)
        if line1 == line2:
            return _('There are no changes in revisions.')
        else:
            diff = difflib.HtmlDiff()
            return diff.make_table(
                line1, line2,
                "Revision-{}".format(v1),
                "Revision-{}".format(v2),
                context=True
            )

    @api.multi
    def name_get(self):
        result = []
        for rec in self:
            name = "%s #%i" % (rec.syllabus_id.name, rec.id)
            result.append((rec.id, name))
        return result
