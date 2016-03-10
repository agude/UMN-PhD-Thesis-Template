# Preliminaries

The various files in this directory are used to format the title, abstract,
and messages from the author.

## title.tex

The [title.tex](title.tex) file is where the title is set, as well as the
author's name, advisor's name, and date. It includes the `\draft` switch
which will turn draft mode on or off, and the `\phd` and `\ms` switches which
set up the thesis for a Doctorate or Master thesis. It also includes three
switches to set the copyright page of the thesis:

- `\copyrightpage`: Full copyright
- `\copyrightpageccby`: Full copyright with Creative Commons CC-BY 4.0 license
- `\copyrightpageccbysa`: Full copyright with Creative Commons CC-BY-SA 4.0 license

A note about the title; the guidelines state:

> "The title of the thesis must not contain chemical or mathematical formulas,
> symbols, superscripts, subscripts, Greek letters, or other non-standard
> characters; words must be substituted."

## acknowledge.tex

The [acknowledge.tex](acknowledge.tex) file is where an acknowledgment can be
written. Including it is optional. It can be disabled in
[title.tex](title.tex).

## dedication.tex

The [dedication.tex](dedication.tex) file is where a short dedication can be
written. Including it is optional. It can be disabled in
[title.tex](title.tex).

## abstract.tex

The [abstract.tex](abstract.tex) file is where a short summary of the thesis
can be written. Including it in thesis is optional although an abstract must
be submitted online with the thesis. It can be disabled in
[title.tex](title.tex).
