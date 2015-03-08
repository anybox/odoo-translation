# -*- coding: utf-8 -*-
##############################################################################
#
#    Authors: Pierre VERKEST
#    Copyright (c) 2015 Anybox SAS (http://anybox.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'UI Translation',
    'version': '1.0',
    'author': 'Anybox',
    'maintainer': 'Anybox Team',
    'website': 'http://anybox.fr',
    'category': 'Anybox',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'web_imports.xml',
        'translate_wizard.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
}
