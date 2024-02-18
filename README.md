# Schneider et al. 2024
Code for all data analyses in Schenider et al. 2024 (JCI). Data files are available at: [OSF | Bap1_Schneider2024](https://osf.io/jgnve/)


# Analyses
## Seurat (Seurat)
- Pre-processing, integration, cluster markers, and differential expression (R): [Seurat/MainAnalysis/](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/Seurat/MainAnalysis)


## RNA velocity analysis (RNAVelocity)
- Pre-processing data from Seurat (R): `Seurat_extract_data_glia+neurons.Rmd` in [RNAVelocity](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/RNAVelocity)
- velocyto (sh): `velocyto_glia+neurons.sh` in [RNAVelocity](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/RNAVelocity)
- scVelo (py): `RNA_velocity_scvelo_analysis_wt_glia+neurons_V1.1.py` and `RNA_velocity_scvelo_analysis_ko_glia+neurons_V1.1.py` in [RNAVelocity](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/RNAVelocity)


# Pathway analysis
**Neuron**
- MSigDB overlap analysis (R): `MSigDBOverlap_Neuron_KO_v_WT_V1.1.Rmd` in [DEGPathwayAnalysis](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/DEGPathwayAnalysis)
- fgsea analysis (R): `fgsea_Neuron_KO_v_WT_V1.Rmd` in [DEGPathwayAnalysis](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/DEGPathwayAnalysis)

**Glia**
- MSigDB overlap analysis (R): `MsigDBOverlap_Glia_KO_v_WT_v1.1.Rmd` in [DEGPathwayAnalysis](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/DEGPathwayAnalysis)
- fgsea analysis (R): `fgsea_Glia_KO_v_WT_V1.Rmd` in [DEGPathwayAnalysis](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/DEGPathwayAnalysis)
