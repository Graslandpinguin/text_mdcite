# text_mdcite
MoinMoin - Parser for a Markdown - Citation

    Creates my own style citations with markdown. Reduces typing.
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
>citation
>   
> – [Author](link)

##Installation

tested with Moin 1.9.8

For general installation instructions, see [ParserMarket/InstallingParsers](https://moinmo.in/ParserMarket/InstallingParsers). This parser requires the Python Markdown library.

## Copyright
Copyright 2015 Simon Lenz

heavily based on the moinmoin markdown parser by Jason R. Fruit.
https://moinmo.in/ParserMarket/Markdown
 
## License
released under GPL-3

for more information see LICENCE document
