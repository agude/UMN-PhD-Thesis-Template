# Build PDF by default
$pdf_mode = 1;

# Use pdflatex with non-interactive mode
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error %O %S';
