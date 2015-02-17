# -*- coding: utf-8 -*-
#
#
#    Author: Romain Deheele
#    Copyright 2015 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

{'name': 'Opportunity Lost Reason',
 'version': '1.0',
 'author': 'Camptocamp',
 'category': 'Customer Relationship Management',
 'license': 'AGPL-3',
 'complexity': 'normal',
 'images': [],
 'website': "http://www.camptocamp.com",
 'description': """
Opportunity Lost Reason
=======================

When an opportunity is lost, a reason must be given,
it is chosen from a configured list.
(strongly inspired from sale_cancel_reason addon)

""",
 'depends': ['crm',
             ],
 'demo': [],
 'data': ['wizard/lost_reason_view.xml',
          'view/crm_lead_view.xml',
          'security/ir.model.access.csv',
          'data/crm_lead_lost_reason.xml',
          ],
 'auto_install': False,
 'test': ['test/crm_lead_lost.yml',
          ],
 'installable': True,
 }
