# Schneider et al. 2024
Code for all data analyses in Schenider et al. 2024. Data files are available at: [OSF | Bap1_Schneider2024](https://osf.io/jgnve/)


# Analyses

The analyses for this paper are separated into three main components:

## `Seurat/`
Pre-processing, integration, cluster markers, and differential expression.
  - `MainAnalysis/`: Quality filtering, integration of WT and _TyrBap1_ KO samples, identifying cell types, cluster marker identification for neurons and glia. Neurons and glia were identified and analyzed separately. Includes initial differential expression analysis of neurons (but not glia).
  - `DifferentialExpressionAnalysis/`: differential expression (using Seurat between WT and _TyprBap1_ KO across all clusters and for each individual cluster). This differential expression analysis is set up the same way as the DE analysis in `MainAnalysis/`, just with more formalized code to produce a standardized output for both neurons and glia.
  - `IntegrationAllCells/`: Integration of WT and _TyrBap1_ KO samples neurons and glia to produce UMAP coordinates and cell types metadata for RNA velocity visualizations. Cell types were pulled from `MainAnalysis/` data, matched barcodes to assign cell types in this integration, integration was performed, and the resulting Seurat object was saved (h5Seurat) and converted to .h5ad for RNA velocity analysis input.

  
## `RNAVelocity/`
RNA velocity analysis using veloctyo and scVelo.
- This analysis uses `velocyto` to get unspliced and spliced counts from the CellRanger outs (available on GEO).
  - velocyto (sh): `velocyto_glia+neurons.sh` in [RNAVelocity](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/RNAVelocity)
- The `velocyto` count matrices (.loom file) was filtered to retain only cells in the processed Seurat data (as .h5ad file), then the two AnnData objects were merged using `scv.utils.merge()`. The purpose of this is to make an AnnData object with the count matrices where the cell barcodes have the metadata (celltypes, UMAP coordinates) as determined in the Seurat analysis. scVelo was run on the merged object according to the [scVelo](https://scvelo.readthedocs.io/en/stable/VelocityBasics/) instructions for the dynamical model.
  - Pre-processing data from Seurat (R): `Seurat_extract_data_glia+neurons.Rmd` in [RNAVelocity](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/RNAVelocity)
  - scVelo (py): `RNA_velocity_scvelo_analysis_wt_glia+neurons_V1.1.py` and `RNA_velocity_scvelo_analysis_ko_glia+neurons_V1.1.py` in [RNAVelocity](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/RNAVelocity)


## `DEGPathwayAnalysis/`
Pathway analysis using the differentially expressed genes from `Seurat/DifferentialExpressionAnalysis/`.

**MSigDB overlap analysis**
  - Preparation of gene lists for MSigDB overlap analysis (https://www.gsea-msigdb.org/gsea/msigdb/mouse/annotate.jsp) using the top genes (maximum 200 genes) up in WT and top genes (maximum 200 genes) up in _TyprBap1_ KO. Includes instructions for plotting of data from MSigDB overlap analysis as dotplot.
    - **Neuron** MSigDB overlap analysis: `MSigDBOverlap_Neuron_KO_v_WT_V1.1.Rmd` in [DEGPathwayAnalysis](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/DEGPathwayAnalysis)
    - **Glia** MSigDB overlap analysis: `MsigDBOverlap_Glia_KO_v_WT_v1.1.Rmd` in [DEGPathwayAnalysis](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/DEGPathwayAnalysis)

**Gene set enrichment analysis analysis**
  - `fgsea` analysis using all genes output from the `DifferentialExpressionAnalysis/`, ranked by `avg_log2FC` (calculated from `avg_logFC`).
    - **Neuron** fgsea analysis (R): `fgsea_Neuron_KO_v_WT_V1.Rmd` in [DEGPathwayAnalysis](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/DEGPathwayAnalysis)
    - **Glia** fgsea analysis (R): `fgsea_Glia_KO_v_WT_V1.Rmd` in [DEGPathwayAnalysis](https://github.com/HeuckerothLab/Bap1_Schneider2024/tree/main/DEGPathwayAnalysis)
