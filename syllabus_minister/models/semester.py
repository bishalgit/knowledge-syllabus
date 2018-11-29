from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)



class Semester(models.Model):
    _name = 'syllabus_minister.semester'
    _description = 'Semester'
    _inherit = 'mail.thread'
    _order =  'sequence, id'

    name = fields.Char(string='Semester')
    sequence = fields.Integer(string='sequence',default=1)

    # _sql_constraints = [
    #      ('name_unique', 'unique(name)','Semester must be unique')]