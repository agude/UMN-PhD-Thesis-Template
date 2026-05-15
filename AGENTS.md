# AGENTS.md

## Project Overview

University of Minnesota PhD/MS thesis LaTeX template. Uses the custom
`mnthesis` document class (based on `report`) that implements UMN Graduate
School formatting requirements.

## Build Commands

```bash
make        # Build thesis.pdf (keeps intermediate files)
make tidy   # Build thesis.pdf and clean intermediate files
make clean  # Remove all generated files including PDF
```

Docker (no local TeX Live required):

```bash
make docker        # Build thesis.pdf
make docker-tidy   # Build and clean intermediate files
make docker-clean  # Remove all generated files
```

## Structure

- `thesis.tex` - Main document, controls chapter inclusion via `\includeonly`
- `mnthesis.cls` - Document class implementing UMN formatting
- `my_definitions.tex` - Custom macros and package configuration
- `chapters/` - Chapter content files
- `preliminaries/` - Title, abstract, acknowledgments, dedication
- `figures/` - Image files
- `thesis.bib` - Bibliography database (uses `hunsrt.bst` style)

## Key Packages

The template configures these packages with specific settings:

- **siunitx**: Use `\SI{value}{unit}` for quantities, `\num{}` for numbers.
  Configured for comma grouping and serial comma in lists.
- **cleveref**: Use `\cref{}` instead of `\ref{}` for automatic prefixes.
  Configured with `noabbrev` and serial comma.
- **booktabs**: Use `\toprule`, `\midrule`, `\bottomrule` for tables.

## Document Class Options

In `mnthesis.cls`, thesis metadata is set via:
- `\title{}`, `\author{}`, `\director{}`
- `\submissionyear{}`, `\submissionmonth{}`
- `\phd` or `\ms` for degree type
- `\copyrightpage`, `\copyrightpageccby`, `\copyrightpageccbysa` for copyright
  options
