# University of Minnesota Thesis Template

A LaTeX template for University of Minnesota PhD dissertations and Master's
theses, meeting Graduate School formatting requirements.

## Getting Started

1. Click **"Use this template"** → **"Create a new repository"**
2. Clone your new repository
3. Edit `preliminaries/title.tex` with your information
4. Start writing in `chapters/`

## Building Your Thesis

### Local (Ubuntu/Debian)

```bash
sudo apt-get install texlive-latex-base texlive-latex-extra \
    texlive-fonts-recommended texlive-pictures texlive-science latexmk

make        # Build thesis.pdf
make tidy   # Build and clean intermediate files
make clean  # Remove all generated files
```

### GitHub Actions

Push to GitHub and the PDF builds automatically. Go to the **Actions** tab,
click a successful build, and download "Compiled Thesis" from **Artifacts**.

### Overleaf

Upload or import your clone of the repository to
[Overleaf](https://www.overleaf.com/). It works out of the box.

## Project Structure

```
thesis.tex              # Main document
preliminaries/
    title.tex           # Title, author, advisor, degree type
    abstract.tex        # Abstract
    acknowledge.tex     # Acknowledgements
    dedication.tex      # Dedication
chapters/
    intro.tex           # Chapter files
    ...
figures/                # Images and graphics
thesis.bib              # Bibliography
my_definitions.tex      # Custom macros
mnthesis.cls            # Document class (don't edit unless necessary)
```

## Configuration

In `preliminaries/title.tex`:

```latex
\phd                            % Use \ms for Master's thesis
\title{Your Title}
\author{Your Name}
\director{Advisor Name}
\submissionmonth{May}
\submissionyear{2025}

% Copyright options (uncomment one):
\copyrightpage                  % Standard copyright
%\copyrightpageccby             % Creative Commons CC-BY
%\copyrightpageccbysa           % Creative Commons CC-BY-SA
```

## Included Packages

### cleveref

Smart cross-references that automatically add "Figure", "Table", etc.

```latex
\cref{fig:example}              % "Figure 1"
\cref{fig:a,fig:b,fig:c}        % "Figures 1, 2, and 3"
```

### siunitx

Consistent formatting for numbers and SI units.

```latex
\num{12345}                     % "12,345"
\SI{9.8}{\meter\per\second^2}   % "9.8 m/s²"
\SIrange{1}{10}{\kilo\gram}     % "1 kg to 10 kg"
```

### booktabs

Professional tables with `\toprule`, `\midrule`, `\bottomrule`.

```latex
\begin{tabular}{@{}lr@{}}
    \toprule
    Item    & Value \\
    \midrule
    Alpha   & 1.0 \\
    Beta    & 2.0 \\
    \bottomrule
\end{tabular}
```

## History

This template has been maintained by UMN students since 1989. See the header
of `mnthesis.cls` for the full list of contributors.
