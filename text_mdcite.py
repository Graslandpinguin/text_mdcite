# -*- coding: utf-8 -*-
# 
# text_mdcite a moinmoin parser for markdown styled citations.
#
# Copyright 2015 Simon Lenz
#
#
# heavily based on the moinmoin markdown parser by Jason R. Fruit.
# https://moinmo.in/ParserMarket/Markdown
# 
# Copyright by Jason R. Fruit
#
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
#

from markdown import markdown

# for html sanitizing
import bleach

Dependencies = ['user']

class Parser:
    """
    A thin wrapper around a Python implementation
    (http://www.freewisdom.org/projects/python-markdown/) of John
    Gruber's Markdown (http://daringfireball.net/projects/markdown/)
    to make it suitable for use with MoinMoin.
    """

    extensions = ['.md']

    def __init__(self, raw, request, **kw):
        self.raw = raw
        self.request = request
	
    def format(self, formatter):
        # clean input from malicious code
        sanitized_input = bleach.clean(self.raw)
        lines = sanitized_input.splitlines()

        author = lines[0]
        link = lines[1]
        citation_lines = lines[2:]

        # prefix every line of the citation body with a ">"
        output_md = ">"
        output_md += "\n>".join(citation_lines)
        output_md += "\n>\n"
        output_md += u" – <cite>[{}]({})</cite>".format(author, link)
        output_html = markdown(output_md)

        try:
            self.request.write(formatter.rawHTML(output_html))
        except:
            self.request.write(formatter.escapedText(output_html))
