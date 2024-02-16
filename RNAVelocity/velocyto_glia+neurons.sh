#!/bin/bash
# run velocyto for the Wild-type data
# The input data for this analysis are available on Gene Expression Omnibus (GEO) and Sequence Read Archive (SRA) (see associated publication)
velocyto run --outputfolder RNAVelocity/DataObjects/Wildtype/ \
--samtools-threads 16 --samtools-memory 2000 \
--bcfile WT_barcodes.tsv \
--mask references/mm38/GRCm38_rmsk.gtf \
WT_possorted_genome_bam.bam \
references/mm38/cellranger_ref/refdata-gex-mm10-2020-A/genes/genes.gtf

# run velocyto for the Knockout data
# The input data for this analysis are available on Gene Expression Omnibus (GEO) and Sequence Read Archive (SRA) (see associated publication)
velocyto run --outputfolder RNAVelocity/DataObjects/Knockout/ \
--samtools-threads 16 --samtools-memory 2000 \
--bcfile KO_barcodes.tsv \
--mask references/mm38/GRCm38_rmsk.gtf \
KO_possorted_genome_bam.bam \
references/mm38/cellranger_ref/refdata-gex-mm10-2020-A/genes/genes.gtf
