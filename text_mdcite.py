# -*- coding: utf-8 -*-

"""
    MoinMoin - Parser for a Markdown - Citation

    creates my own citation style with markdown. Reduces typing.

    Based on: https://moinmo.in/ParserMarket/Markdown

    Syntax:

        To use in a code block:
    
            {{{#!text_mdcite
            <Author>
            <Link>
            <add markdown citationtext here>
            }}}

        creates:

            <blockquote>
            citation

             – [Author](link)
            </blockquote>

"""

from markdown import markdown

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

        try:
            self.args = request.cfg.markdownargs
        except AttributeError:
            self.args = { 'safe_mode': 'replace' }
	
    def format(self, formatter):
        lines = self.raw.splitlines()

        author = lines[0]
        link = lines[1]
        citation_lines = lines[2:]

        output_md = ">"
        output_md += "\n>".join(citation_lines)

        output_md += "\n>\n"
        output_md += u" – [{}]({})".format(author, link)

        output_html = markdown(output_md, **self.args)
        try:
            self.request.write(formatter.rawHTML(output_html))
        except:
            self.request.write(formatter.escapedText(output_html))
