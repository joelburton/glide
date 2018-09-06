"""Directive to stop make-ing in its tracks until directive is removed from RST
file. The point is to force the person trying to build the slides/html/etc to
deal with whatever note is in the directive before they can proceed, so that
TODO's about super-important changes to lectures, etc don't get missed. """

from docutils.parsers.rst import Directive
import logging
import sys
import os


class RequiredDirective(Directive):
    """Directive that raises an error and prevents building."""

    #copied from noplot.py - is there any reason we need this?
    has_content = True


    def run(self):

        text = "\n".join(self.content)
        error = ("\n\n\nERROR: REQUIRED DIRECTIVE FOUND. Please read and " +
                 "remove from the RST before trying to build again. " +
                 "The content of the directive is as follows:\n\n" + text +
                 "\n\n---")

        #raising an exception is probably preferable, but looks-wise, it bugs me
        #because the final \n\n gets stripped off of the error message; this
        #doesn't happen when the error is logged instead, but then we need some
        #way to make everything come crashing to a halt, and none of the exit
        #functions seem to be working
        # raise Exception(error)
        logging.error(error)
        os._exit(1)

        #None of the below seem to kill the process in its tracks, which I
        #don't understand
        # logging.shutdown()
        # exit()
        # sys.exit()

        #If we've logged the error (rather than raised an exception), returning
        #something other than a list of nodes causes an exception and stops
        #things
        # return -1


def setup(app):
    """Sphinx directive setup."""

    app.add_directive('required', RequiredDirective)
