# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class CurricularStructureParser(models.AbstractModel):
    _name = 'report.syllabus_syllabus.report_program_old_version_view'

    def get_next_neighbor_size(self, obj, semester_index):
        if ((semester_index % 2) == 0):
            next_index = semester_index + 1
        else:
            next_index = semester_index - 1
        
        semester_index_course_line_ids_size = len(obj.courseline_ids.filtered(lambda x: obj.semester_id[semester_index] == x.semester))
        next_index_course_line_ids_size = len(obj.courseline_ids.filtered(lambda x: obj.semester_id[next_index] == x.semester))
        
        if (semester_index_course_line_ids_size < next_index_course_line_ids_size):
            size = abs(semester_index_course_line_ids_size - next_index_course_line_ids_size)
            content = ""
            print("************************************************************************************************")
            print(size)
            for _ in range(size):
                content = content + """<tr>
                    <td>
                        <p style='text-align:left; line-height: normal;'>
                            <span style="font-family: 'Times New Roman',serif;">-</span>
                        </p>
                    </td>
                    <td>
                        <p style='text-align:left; line-height: normal;'>
                            <span style="font-family: 'Times New Roman',serif;">-</span>
                        </p>
                    </td>
                    <td>
                        <p style='text-align:left; line-height: normal;'>
                            <span style="font-family: 'Times New Roman',serif;">-</span>
                        </p>
                    </td>
                </tr>"""
            return content
        
        return ''

    @api.model
    def get_report_values(self, docids, data=None):
        programs = self.env['syllabus_minister.program'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'syllabus_minister.program',
            'data': data,
            'docs': programs,
            'get_next_neighbor_size': self.get_next_neighbor_size,
        }