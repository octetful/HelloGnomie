# window.py
#
# Copyright 2019 Siddhartha Ghosh
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk


@Gtk.Template(resource_path='/com/octetful/gnome/window.ui')
class HellognomieWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'HellognomieWindow'

    display_label = Gtk.Template.Child()
    entry_text = Gtk.Template.Child()
    click_btn = Gtk.Template.Child()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.click_btn.connect('clicked', self.say_hello)

    def say_hello(self, widget):
        self.display_label.set_label(self.entry_text.get_text())
