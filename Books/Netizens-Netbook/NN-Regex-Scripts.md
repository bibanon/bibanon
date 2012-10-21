## Netizens Netbook replace scripts

### Remove all spaces at end of lines (which prevent markdown line wrapping)

    |s \s+$
    |g 

### Replace --- and ___ titles with ### ones

    |s \n(?:_)+\n(.+)|\n(?:-)+\n(.+)
    |g \n\n### \1

### Remove all indents

    |s ^\s+
    |g 
    
### Replace 1) with 1.

    |s ^(\d)\)
    |g \1.
    
### Replace (1) with 1.

    |s ^\s*\((\d+)\)
    |g \1.