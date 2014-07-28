
import gtk as Gtk
import os
import signal

from pprint import pprint

class window(Gtk.Builder):
	"""docstring for window"""

	def __init__(this):
		super(window, this).__init__()
		this.add_from_file(os.path.join(os.path.dirname(__file__), 'window.glade'))
		this.connect_signals(this)

		this.window = this.get_object("window")
		this.window.show_all()


	def main(this):
		signal.signal(signal.SIGINT, signal.SIG_DFL)
		Gtk.main()
