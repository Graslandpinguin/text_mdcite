# text_mdcite
MoinMoin - Parser for a Markdown - Citation

    creates markdown citations. 

    reduces typing.

    style from http://stackoverflow.com/a/2002150/376172

##Dependencies
 * python markdown library

##Syntax:

To use in a code block:
    
    {{{#!text_mdcite
    <Author>
    <Link>
    <multiline citationtext here (in markdown syntax)>
    }}}

creates:

    <blockquote>
      <p>markdown2html citation body</p>
      <p>– <cite><a href="https://en.wikipedia.org/wiki/Multi-licensing#Business_models">Wikipedia</a></cite>
      </p>
    </blockquote>

which will be rendered as:

>citation
>   
> – <cite>[Author](link)</cite>

##Installation

tested with Moin 1.9.8

For general installation instructions, see [ParserMarket/InstallingParsers](https://moinmo.in/ParserMarket/InstallingParsers). 

This parser requires the Python Markdown library and [bleach](https://github.com/mozilla/bleach).

## Copyright
Copyright 2015 Simon Lenz

heavily based on the moinmoin markdown parser by Jason R. Fruit.

https://moinmo.in/ParserMarket/Markdown
 
## License
released under GPL-3

for more information see LICENCE document
