# Bap1
Code for Bap1 analyses


# Analyses
## Seurat (Seurat)
- Pre-processing, integration, cluster markers, and differential expression: [Seurat/MainAnalysis/](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/Seurat/MainAnalysis)


## RNA velocity analysis (RNAVelocity)
- Pre-processing data from Seurat (R): `Seurat_extract_data_glia+neurons.Rmd` in [RNAVelocity](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/RNAVelocity)
- velocyto (sh): `velocyto_glia+neurons.sh` in [RNAVelocity](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/RNAVelocity)
- scVelo (py): `RNA_velocity_scvelo_analysis_wt_glia+neurons_V1.1.py` and `RNA_velocity_scvelo_analysis_ko_glia+neurons_V1.1.py` in [RNAVelocity](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/RNAVelocity)


# Pathway analysis
Neuron
- MSigDB overlap analysis
- fgsea analysis

Glia
- MSigDB overlap analysis
- fgsea analysis
