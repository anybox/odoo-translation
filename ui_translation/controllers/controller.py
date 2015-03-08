# -*- coding: utf-8 -*-
from openerp import http
from openerp.tools.translate import _


class UITranslationControler(http.Controller):

    @http.route('/web/ui_translation/get_translate_wizard', type='json', auth='user')
    def get_translate_wizard(self, request, **context):
        model = context.get('model', False)
        translate_label = context.get('label', False)
        if not translate_label:
            return {'value': _("Label not found"), 'is_action': False}

        view = request.env.ref('ui_translation.translate_form')
        res_id = request.env['ui.translate.translate.wizard'].create(
            {'name': translate_label,
             'label_model': model, })
        context.update(request.env.context)
        return {'value': {'name': _('Odoo UI Translate'),
                          'type': 'ir.actions.act_window',
                          'view_type': 'form',
                          'view_mode': 'form',
                          'res_model': 'ui.translate.translate.wizard',
                          'views': [(view.id, 'form')],
                          'view_id': view.id,
                          'res_id': res_id.id,
                          'target': 'new',
                          'context': context, },
                'is_action': True}
