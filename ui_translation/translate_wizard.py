# -*- coding: utf-8 -*-
from openerp import models, fields, api


class TranslateWizard(models.TransientModel):

    _name = 'ui.translate.translate.wizard'
    _description = u"Transient model to translate odoo terms"

    name = fields.Char(u"Label", help=u"Label to translate, where you clicked")
    label_model = fields.Char(u"Label's model",
                              help=u"Reference model to restricted results,\n"
                                   u"this is used to accurate string to "
                                   u"translate")
    user_lang = fields.Char(u"Translating lang.",
                            help=u"Translating language",
                            default=lambda self: self.env.context.get('lang', False))
    expected_translation_ids = fields.Many2many(
        'ir.translation',
        string=u"Translate zone",)

    @api.model
    def create(self, values):
        # TODO: extract domain construction outside this method
        domain = [('name', 'ilike', values.get('label_model'))
                  ] if values.get('label_model', False) else []
        domain.extend([('lang', '=ilike', self.env.context.get('lang', False)),
                       '|', ('src', '=like', values.get('name', False)),
                       ('value', '=like', values.get('name', False))])
        ids = self.env['ir.translation'].search(domain).ids
        values.update({'expected_translation_ids': [(6, False, ids)]})
        res = super(TranslateWizard, self).create(values)
        return res

    @api.one
    def translate(self):
        self.env['ir.translation'].clear_caches()
        self.env['ir.translation'].clear_caches()
        self.env['ir.ui.view'].clear_caches()
        self.env['ir.ui.menu'].clear_caches()
        return True
        """
        It could be nice if we could send the result to the client
        to refresh only changed labels
        res = [(trans.src, trans.value, trans.type)
               for trans in self.expected_translation_ids]
        return {'value': res}
        """

"""
id       | 3408
lang     | fr_FR
src      | Address
name     | res.partner
res_id   | 0
module   | base
state    | translated
value    | Adresse
type     | view
comments |


    translate_id
    lang
    source
    existed
    type
"""
