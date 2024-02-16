# Seurat Analysis
scRNa data were analyzed in Seurat v3.1.2. The directories here contain different aspects of the Seurat scRNA analysis.

## `MainAnalysis`
S. Schneider's main analysis scripts for pre-processing (filtering) scRNA data and generating the initial differential expression results.

## `DifferentialExpressionAnalysis`
K. Beigel's replication of S. Schneider's differential expresison analysis, using updated cluster names. The purpose of this was to make sure the resulting files were standardized and that S. Schenider's process was reproducible.

## `IntegrationRNAVelocityPrep`
K. Beigel's integration script for combining glia and neuron WT and KO samples in Seurat v4 object, which was necessary data preparation for RNA velocity analysis.
