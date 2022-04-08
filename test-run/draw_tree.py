from Bio import Phylo
from matplotlib import pyplot as plt

# first set PATH for quicktree
# export PATH=/Users/mbr5797/PSU/Research/neighbor-joining/quicktree-master:$PATH
# then run quicktree -m  distance_matrix > out
# then activate environment that has Bio, matplotlib and pyplot (bioconda in your machine)
# then run this script

tree = Phylo.read("out", "newick")
tree.ladderize()
Phylo.draw(tree, do_show=False)
plt.savefig('phylo_tree.pdf')
