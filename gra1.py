

#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import threading
import time

import networkx as nx # 00
import xdot
import gtk

class MyClass(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.graph = nx.DiGraph(name="my_tree")
        self.xdot = xdot.DotWindow()
        self.xdot.connect('destroy', gtk.main_quit)

    def run(self):
        gtk.main()

    def add_node(self, parent, node):

        self.graph.add_edge(parent, node)
        self.xdot.set_dotcode(nx.to_agraph(self.graph).to_string())
        self.xdot.show_all()

def main(argv=None):

    gtk.gdk.threads_init()
    my_class = MyClass()
    my_class.start()

    my_class.add_node(1, 2)
    time.sleep(0.5)
    my_class.add_node(1, 3)
    time.sleep(0.3)
    my_class.add_node(2, 4)
    time.sleep(1.3)
    my_class.add_node(2, 5)
    my_class.add_node(1, 6)

if __name__ == "__main__":
    sys.exit(main())
