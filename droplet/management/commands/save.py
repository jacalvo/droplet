# -*- coding: utf-8 -*-
#
#  droplet
#  Copyright (C) 2014 Carlos Pérez-Aradros Herce <exekias@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.core.management.base import BaseCommand, CommandError
from droplet import modules


class Command(BaseCommand):
    help = 'Save a module conf files'

    def handle(self, *args, **kwargs):
        names = [n.upper() for n in args]
        for module in modules():
            if module.verbose_name.upper() in names:
                if module.enabled:
                    module.save()
                    names.remove(module.verbose_name.upper())

                else:
                    raise CommandError('Module %s is disabled' %
                                       module.verbose_name)

        if names:
            raise CommandError('Module %s does not exist' % ','.join(names))