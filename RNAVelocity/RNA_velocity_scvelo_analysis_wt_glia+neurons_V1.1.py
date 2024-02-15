#!/usr/bin/env python
# coding: utf-8

# # RNA Velocity analysis using velocyto, Seurat, and scVelo (Part 2: Analysis)
# ## For WILD-TYPE (wt) sample GLIA+NEURONS -- VERSION 1.1
# ### Kat Beigel (beigelk@chop.edu)
# #### 7/21/23

# See the following pages for guides on how to combine Seurat and velocyto data for scVelo analysis and visualization.
# https://scvelo.readthedocs.io/en/stable/VelocityBasics/
# https://smorabit.github.io/tutorials/8_velocyto/

# In[2]:


import anndata
import scanpy as sc
import scvelo as scv
import pandas as pd
import numpy as np
import matplotlib as plt
import loompy as lpy
from scipy.stats import rankdata


# In[3]:


print(np.__version__)
print(sc.__version__)
print(scv.__version__)
print(anndata.__version__)


# In[3]:


# Load the wt data
adata_seurat = sc.read_h5ad('scRNA_data/wt_glia+neurons_seurat_V1.h5ad')
print(adata_seurat)


# In[4]:


adata_loom = anndata.read_loom("scRNA_data/Wild-type/velocyto_loom/V3/possorted_genome_bam_EKIP1.loom")
print(adata_loom)


# In[5]:


print(adata_loom.obs.index)


# In[6]:


barcodes = [('WT_'+(bc.split(':')[1]).replace('x', '')) for bc in adata_loom.obs.index.tolist()]
adata_loom.obs.index = barcodes
print(adata_loom.obs.index)


# In[7]:


adata_loom = adata_loom[np.isin(adata_loom.obs.index, adata_seurat.obs.index)].copy()
print(adata_loom)


# In[8]:


print(adata_loom.obs)
print(adata_seurat.obs)


adata_all = scv.utils.merge(adata_loom, adata_seurat, copy = True)
print(adata_all.obs)


# In[9]:


print(adata_all.obsm['X_umap'])


# In[10]:


for col in ['orig.ident', 'seurat_clusters', 'seurat_clusters_neurons', 'cluster_numbers_in_paper']:
    adata_all.obs[col] = adata_all.obs[col].astype('category')


# In[11]:


adata_all.obs['cluster_numbers_in_paper']


# ### Running scvelo

# In[12]:


scv.settings.verbosity = 3


# In[13]:


scv.settings.presenter_view = True


# In[14]:


scv.set_figure_params('scvelo')


# In[15]:


cell_type_list = [
   "Glia",
   "Undecided neuroblast",
   "Undecided neuroblast-2",
   "Nitrergic neuroblast",
   "Immature inhibitory motor neuron/ENC9",
   "Inhibitory motor neuron/ENC9",
   "Confused neuron",
   "Cholinergic neuroblast",
   "Cholinergic neuroblast-2",
   "Excitatory motor neuron/ENC1",
   "Excitatory motor neuron/ENC3?",
   "Immature excitatory motor neuron/ENC4",
   "Excitatory motor neuron/ENC4",
   "Interneuron/ENC12",
   "IPAN/ENC6"]


cluster_nums_list = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

# Using list comprehension
cluster_nums_list = [str(x) for x in cluster_nums_list]
print(cluster_nums_list)

color_list = ["#DCDCDC",
               "#F8766D",
               "#E38900",
               "#C49A00",
               "#99A800",
               "#53B400",
               "#00BC56",
               "#00C094",
               "#00BFC4",
               "#00B6EB",
               "#06A4FF",
               "#A58AFF",
               "#DF70F8",
               "#FB61D7",
               "#FF66A8"]

palette_cols_celltypes = {}
for key in cell_type_list:
    for value in color_list:
        palette_cols_celltypes[key] = value
        color_list.remove(value)
        break
        
        
color_list = ["#DCDCDC",
               "#F8766D",
               "#E38900",
               "#C49A00",
               "#99A800",
               "#53B400",
               "#00BC56",
               "#00C094",
               "#00BFC4",
               "#00B6EB",
               "#06A4FF",
               "#A58AFF",
               "#DF70F8",
               "#FB61D7",
               "#FF66A8"]
        
palette_cols_clustnum = {}
for key in cluster_nums_list:
    for value in color_list:
        palette_cols_clustnum[key] = value
        color_list.remove(value)
        break
        
print(palette_cols_celltypes)
print(palette_cols_clustnum)


# In[16]:


# https://github.com/scverse/scanpy/issues/1648
plt.rcParams.update({'font.size': 5})
sc.pl.umap(adata_all, color='cell_type', frameon=False, legend_loc='on data',
           title='Wild-type', palette = palette_cols_celltypes,
           save='_wt_glia+neurons_umap_cell_types_V1.1.pdf')

plt.rcParams.update({'font.size': 10})
sc.pl.umap(adata_all, color='cluster_numbers_in_paper', frameon=False, legend_loc='on data',
           title='Wild-type', palette = palette_cols_clustnum,
           save='_wt_glia+neurons_umap_neuron_clusters_V1.1.pdf')


# In[17]:


scv.pl.proportions(adata_all, fontsize=8, figsize=(20, 5), dpi=(300), groupby='cell_type',
                   save = 'wt_glia+neurons_V1.1.pdf')


# In[18]:


# https://github.com/theislab/scvelo/issues/1052
scv.pp.filter_and_normalize(adata_all)


# In[19]:


scv.pp.neighbors(adata_all)


# In[20]:


scv.pp.moments(adata_all)


# In[21]:


scv.tl.recover_dynamics(adata_all) # for dynamical model


# In[22]:


scv.tl.velocity(adata_all, mode = "dynamical")


# In[23]:


scv.tl.velocity_graph(adata_all)


# In[24]:


scv.pl.velocity_embedding(adata_all, basis = 'umap', frameon=False,
                          figsize=[15,15],
                          title='Wild-type',
                          save='velocity_embedding_wt_glia+neurons_V1.1.pdf')


# In[44]:


scv.pl.velocity_embedding_grid(adata_all, basis='umap', color='cell_type', scale=0.25,
                               figsize=[15,15], legend_loc='right margin',
                               arrow_size=1.75, size=200, alpha=1,
                               title='Wild-type', palette = palette_cols_celltypes,
                               save='velocity_embedding_grid_wt_glia+neurons_V1.1.pdf')


# In[46]:


scv.pl.velocity_embedding_grid(adata_all, basis='umap', color='cell_type', scale=0.25,
                               figsize=[15,15], legend_loc='right margin',
                               arrow_size=1.75, size=50, alpha=1,
                               title='Wild-type', palette = palette_cols_celltypes,
                               save='velocity_embedding_grid_wt_glia+neurons_smallpoints_V1.1.pdf')


# In[47]:


scv.pl.velocity_embedding_grid(adata_all, basis='umap', color='cell_type', scale=0.25,
                               figsize=[15,15], legend_loc='right margin',
                               arrow_size=1.75, size=200, alpha=0.5,
                               title='Wild-type', palette = palette_cols_celltypes,
                               save='velocity_embedding_grid_wt_glia+neurons_alpha05_V1.1.pdf')


# In[42]:


scv.pl.velocity_embedding_grid(adata_all, basis='umap', color='cell_type', scale=0.25,
                               figsize=[15,15], legend_loc='right margin',
                               arrow_size=3, size=200, alpha=1,
                               title='Wild-type', palette = palette_cols_celltypes,
                               save='velocity_embedding_grid_wt_glia+neurons_bigarrows_V1.1.pdf')


# In[26]:


scv.pl.velocity_embedding_stream(adata_all, basis = 'umap', color='cell_type', legend_fontsize=10,
                                 figsize = [10, 10], arrow_size = 2, legend_loc='right margin',
                                 title='Wild-type', palette = palette_cols_celltypes,
                                 save='velocity_embedding_stream_wt_glia+neurons_legend_V1.1.pdf')


# In[27]:


scv.pl.velocity_embedding_stream(adata_all, basis = 'umap', color='cell_type', legend_fontsize=5,
                                 figsize = [10, 10], arrow_size = 1, palette = palette_cols_celltypes,
                                 title='Wild-type', integration_direction='both',
                                 save='velocity_embedding_stream_wt_glia+neurons_V1.1.pdf')


# Dynamical modeling: https://scvelo.readthedocs.io/en/stable/DynamicalModeling/
# The driver genes (top-likelihood genes) show dynamic behavior (high likelihood in dynamic model).

# In[28]:


top_genes = adata_all.var['fit_likelihood'].sort_values(ascending=False).index
print(top_genes)


# In[29]:


scv.pl.scatter(adata_all, basis=top_genes[:20], ncols=1, color='cell_type', frameon=False,
               palette = palette_cols_celltypes,
               save='wt_glia+neurons_top20_likelihood_genes_celltype_V1.1.pdf')

