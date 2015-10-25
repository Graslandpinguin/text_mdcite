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
