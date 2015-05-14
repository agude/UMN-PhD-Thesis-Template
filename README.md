# University of Minnesota PhD Thesis Template

This repository contains an updated version of the UMN PhD Thesis Template.

## `cleveref`

[`cleveref`](https://www.ctan.org/pkg/cleveref?lang=en) is a package designed
to make cross referencing easier. Unlike `\ref`, `\cref` automatically adds
the prefix required for the object being referenced. For example,
`\cref{fig:my_fig}` will produce text like "figure 1" whereas
`\ref{fig:my_fig}` would simply produce "1" and require you to fill in the
"figure".

Additionally, `cleveref` can handle multiple references at once.
`\cref{fig:my_fig,fig:my_fig2}` produces "figures 1 and 2".

In the [main thesis file](thesis_masters.tex), the following is set:

```latex
\newcommand{\creflastconjunction}{, and } % Always use the serial comma
```

This includes the serial comma in lists, so that
`\cref{fig:my_fig,fig:my_fig2,fig_other_fig}` produces "figures 1, 2, and 3"
instead of "figures 1, 2 and 3".

Additionally, the package is passed the option `noabbrev` which causes it to
print the full prefix instead of an abbreviation ("figure" vs "fig.").
