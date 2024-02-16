# Seurat Analysis
The directories here contain different aspects of the Seurat scRNA analysis.

## `MainAnalysis`
S. Schneider's main analysis scripts for pre-processing (filtering) scRNA data and generating the initial differential expression results. Glia and neuron scRNa data were analyzed separately in Seurat v3.1.2.

## `DifferentialExpressionAnalysis`
K. Beigel's replication of S. Schneider's differential expresison analysis, using updated cluster names. The purpose of this was to make sure the resulting files were standardized and that S. Schenider's process was reproducible. scRNa data were analyzed in Seurat v3.1.2. 

## `IntegrationAllCells`
K. Beigel's integration script for combining glia and neuron WT and KO samples in Seurat object, which was necessary data preparation for RNA velocity analysis. Glia and neuron scRNa data were integrated in Seurat v5.0.1. This integrated data was only used for the RNA velcoity analysis. All other analyses and results were generated using the methods in `MainAnalysis` and `DifferentialExpressionAnalysis`.
