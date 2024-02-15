#!/bin/bash
# run velocyto for the Wild-type data
velocyto run --outputfolder scRNA_data/Wild-type/velocyto_loom/ \
--samtools-threads 16 --samtools-memory 2000 \
--bcfile scRNA_data/Wild-type/outs/filtered_feature_bc_matrix/barcodes.tsv \
--mask /home/beigelk/references/mm38/GRCm38_rmsk.gtf \
scRNA_data/Wild-type/outs/possorted_genome_bam.bam \
references/mm38/cellranger_ref/refdata-gex-mm10-2020-A/genes/genes.gtf

# run velocyto for the Knockout data
velocyto run --outputfolder scRNA_data/Knockout/velocyto_loom/ \
--samtools-threads 16 --samtools-memory 2000 \
--bcfile scRNA_data/Knockout/outs/filtered_feature_bc_matrix/barcodes.tsv \
--mask /home/beigelk/references/mm38/GRCm38_rmsk.gtf \
scRNA_data/Knockout/outs/possorted_genome_bam.bam \
references/mm38/cellranger_ref/refdata-gex-mm10-2020-A/genes/genes.gtf
