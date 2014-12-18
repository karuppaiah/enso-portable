# Copyright (c) 2008, Humanized, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#    3. Neither the name of Enso nor the names of its contributors may
#       be used to endorse or promote products derived from this
#       software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY Humanized, Inc. ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Humanized, Inc. BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# ----------------------------------------------------------------------------
#
#   enso.contrib.help
#
# ----------------------------------------------------------------------------

"""
    An Enso plugin that makes the 'help' command available.
"""

# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------
from __future__ import with_statement

import os
import webbrowser
import tempfile
import urllib
import atexit
import logging

from enso.commands import CommandManager, CommandObject
from enso.contrib.scriptotron.tracebacks import safetyNetted


# ----------------------------------------------------------------------------
# The HTML help system
# ---------------------------------------------------------------------------

class DefaultHtmlHelp( object ):
    """
    HTML help system.  The interface of this system can theoretically
    have multiple implementations that are exposed by Providers.

    At present, this is an extremely 'low-tech' implementation that is
    guaranteed to work on any platform that has a web browser.
    Eventually, different Providers can provide platform-specific
    interfaces that are both secure and humane, e.g. an embedded
    MSIE/WebKit/Mozilla browser that accesses a virtual storage system.
    """

    def __init__( self, commandManager ):
        handle, self.filename = tempfile.mkstemp(
            suffix = ".html",
            prefix = "ensoHelp",
            text = True
            )
        os.close( handle )
        atexit.register( self._finalize )
        self._cmdMan = commandManager

    def _render( self ):
        with open( self.filename, "w" ) as fileobj:
            fileobj.write( "<!DOCTYPE html><html><head><title>Enso Help</title>" )
            fileobj.write("""
                <style>
                body {
                font-family:sans-serif;
                margin:0;
                padding:0;
                }
                h1 {
                background-color:#b2cb78;
                border-radius:0 0 .2em;
                color:white;
                display:inline;
                font-weight:normal;
                padding:.2em;
                }
                ul {
                list-style-type:none;
                margin:1em;
                padding:1em;
                }
                li {
                display:inline;
                line-height:1.5em;
                margin:.2em 1em .2em 0;
                }
                h2 {
                background-color:#272727;
                border-radius:0 .2em .2em 0;
                clear:both;
                color:white;
                display:inline;
                font-weight:normal;
                margin:.4em 0 0 0;
                padding:.2em .8em;
                }
                h3 {
                background-color:#b2cb78;
                color:white;
                display:inline;
                font-weight:normal;
                margin:0;
                padding:.2em .8em;
                }
                p {
                padding:.2em 1em 1em 1em;
                }
                </style>
            """)
            fileobj.write( "</head>" )
            fileobj.write( "<body>" )
            fileobj.write( "<h1>Enso Help</h1>" )

            fileobj.write( "<ul>" )
            for name, command in self._cmdMan.getCommands().items():
                fileobj.write( "<li>" )
                fileobj.write( "<a href=\"#%s\">%s</a>" % (name, name) )
                fileobj.write( "</li>" )
            fileobj.write( "</ul>" )


            for name, command in self._cmdMan.getCommands().items():

                fileobj.write( "<h2 id=\"%s\">%s</h2>" % (name, name) )

                desc = command.getDescription()
                fileobj.write( "<h3>%s</h3>" % desc )

                helpText = command.getHelp()
                #if not helpText:
                #    helpText = "This command has no help content."
                if helpText:
                    helpText = helpText.encode( "utf-8", "xmlcharrefreplace" ).strip()
                else:
                    helpText = ""

                fileobj.write( "<p>%s</p>" %  helpText )

            fileobj.write( "</body></html>" )

    def view( self ):
        self._render()
        fileUrl = "file:%s" % urllib.pathname2url( self.filename )
        # Catch exception, because webbrowser.open sometimes raises exception
        # without any reason
        try:
            webbrowser.open( fileUrl )
        except WindowsError, e:
            logging.warning(e)

    def _finalize( self ):
        os.remove( self.filename )


# ----------------------------------------------------------------------------
# The Help command
# ---------------------------------------------------------------------------

class HelpCommand( CommandObject ):
    """
    The 'help' command.
    """

    NAME = "help"
    DESCRIPTION = "Provides you with help on how to use Enso"

    def __init__( self, htmlHelp ):
        super( HelpCommand, self ).__init__()
        self.setDescription( self.DESCRIPTION )
        self.setName( self.NAME )
        self.__htmlHelp = htmlHelp

    @safetyNetted
    def run( self ):
        self.__htmlHelp.view()


# ----------------------------------------------------------------------------
# Plugin initialization
# ---------------------------------------------------------------------------

def load():
    cmdMan = CommandManager.get()
    cmdMan.registerCommand(
        HelpCommand.NAME,
        HelpCommand( DefaultHtmlHelp(cmdMan) )
        )

# vim:set tabstop=4 shiftwidth=4 expandtab:
