# Figures Directory

Place the figures you want to include in this directory. You may then include
them by using:

```latex
\begin{figure}[!htbp]
    \centering
    \includegraphics[width=\textwidth]{figures/my_figure.pdf}
    \caption[
        %Short caption for the list of figures
        A  figure.
    ]{
        % Full caption shown below the image
        A detailed view of the figure. As you can see, it is very good!
    }
    % A label so you can \ref{fig:my_fig}. It is arbitrary; neither the 'fig:'
    % nor the fact that it has the same name as the pdf are required.
    \label{fig:my_fig}
\end{figure}
```
