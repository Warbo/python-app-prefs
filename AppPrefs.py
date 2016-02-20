#!/usr/bin/env python

#----------------------------------------------------------------------
# AppPrefs.py
# Chris Warburton
# 01/14/2007
#----------------------------------------------------------------------

import sys

from GladeWindow import *

#----------------------------------------------------------------------

class AppPrefs(GladeWindow):

    #----------------------------------------------------------------------

    def __init__(self):

        ''' '''

        self.init()

    #----------------------------------------------------------------------

    def init(self):

        filename = 'AppPrefs.glade'

        widget_list = [
            'window1',
            'label1',
            'label2',
            'label3',
            'button1',
            'button2',
            'image1',
            'image2',
            'combo1',
            ]

        handlers = [
            'browser_picked',
            'close_released',
            ]

        top_window = 'window1'
        GladeWindow.__init__(self, filename, top_window, widget_list, handlers)
   #----------------------------------------------------------------------

    def close_released(self, *args):
        gtk.main_quit()


    #----------------------------------------------------------------------

    def browser_picked(self, *args):
        chosen = self.widgets['combo1'].get_active()
        if chosen == 0:
            self.widgets['label2'].set_text('Firefox is a lightweight, standards compliant browser which can be enhanced with various downloadable plugins.')
            self.widgets['image1'].set_from_file('Images/Icons/Browser.png')
            self.widgets['image2'].set_from_file('Images/Thumbnails/Firefox.png')

        elif chosen == 1:
            self.widgets['label2'].set_text('Epiphany is an easy to use browser which integrates well with the GNOME desktop environment.')
            self.widgets['image1'].set_from_file('Images/Icons/Browser.png')
            self.widgets['image2'].set_from_file('Images/Thumbnails/Epiphany.png')
        else:
            self.widgets['label2'].set_text('Gah!')




#----------------------------------------------------------------------

def main(argv):

    w = AppPrefs()
    w.show()
    gtk.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
