# title: 'Re-analysis of the publication: Splicing factor 1 modulates dietary restriction and TORC1 pathway longevity in _C. elegans_'
# author: Maria Grigorjeva, Yulia Petrova
# date: May 21, 2019


# Downliading in-files
# for downloading fastq-files follow the link https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-4866/


# Quality check [FastQC]
# To assess the quality of the RNA sequencing samples FastQC-analysis was carried out in the FastQC-program without writing any additional code. No samples were excluded.

# Reference files
# to download reference files for _C.elegans_ follow the link http://www.ensembl.org/Caenorhabditis_elegans/Info/Index
# on this site in "WBcel235" point we take reference _C. elegans_ transcriptome
# link for coding DNA ftp://ftp.ensembl.org/pub/release-96/fasta/caenorhabditis_elegans/cdna/
# link for non coding RNA ftp://ftp.ensembl.org/pub/release-96/fasta/caenorhabditis_elegans/ncrna/
cat Caenorhabditis_elegans.WBcel235.cdna.all.fa Caenorhabditis_elegans.WBcel235.ncrna.fa > allna.fa
# combining these files we get all available cDNA information in one file


# cutadapt
# Raw reads were adapter trimmed (the adapter sequences used for RNA-sequencing need to be removed before the reads can be aligned) with cutadapt using the additional parameters “--trim-n -m 15”

pip install --user --upgrade cutadapt
# downloading the cutadapt servese

~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474664_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474664_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474664_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474664_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474665_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474665_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474665_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474665_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474666_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474666_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474666_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474666_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474667_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474667_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474667_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474667_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474668_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474668_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474668_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474668_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474669_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474669_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474669_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474669_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474670_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474670_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474670_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474670_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474671_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474671_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474671_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474671_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474672_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474672_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474672_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474672_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474673_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474673_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474673_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474673_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474674_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474674_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474674_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474674_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474675_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474675_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474675_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474675_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474676_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474676_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474676_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474676_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474677_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474677_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474677_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474677_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474678_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474678_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474678_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474678_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474679_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474679_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474679_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474679_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474686_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474686_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474686_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474686_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474687_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474687_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474687_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474687_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474688_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474688_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474688_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474688_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474689_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474689_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474689_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474689_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474690_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474690_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474690_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474690_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474691_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474691_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474691_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474691_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474692_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474692_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474692_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474692_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474693_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474693_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474693_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474693_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474694_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474694_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474694_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474694_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474695_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474695_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474695_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474695_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474696_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474696_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474696_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474696_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474697_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474697_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474697_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474697_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474698_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474698_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474698_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474698_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474699_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474699_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474699_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474699_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474700_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474700_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474700_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474700_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474701_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474701_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474701_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474701_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474702_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474702_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474702_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474702_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474703_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474703_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474703_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474703_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474704_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474704_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474704_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474704_2.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTCCGAGCCCACGAGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474705_1.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474705_1.fastq
~/.local/bin/cutadapt --trim-n -m 15 -a CTGTCTCTTATACACATCTGACGCTGCCGACGA -o ~/Desktop/inf/term4python/pr/outs/ERR1474705_2.fastq ~/Desktop/inf/term4python/pr/ins/ERR1474705_2.fastq


# STAR version 2.5.0c
# Genome alignment was performed using STAR 2.5.0c.  Additional parameters used for alignment are: _–alignIntronMax 50000_ (WBcel235)
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474664_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474664_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474664
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474665_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474665_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474665
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474666_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474666_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474666
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474667_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474667_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474667
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474668_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474668_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474668
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474669_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474669_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474669
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474670_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474670_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474670
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474671_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474671_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474671
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474672_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474672_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474671
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474673_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474673_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474673
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474674_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474674_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474674
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474675_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474675_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474675
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474676_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474676_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474676
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474677_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474677_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474677
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474678_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474678_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474678
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474679_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474679_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474679
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474686_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474686_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474686
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474687_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474687_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474687
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474688_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474688_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474688
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474689_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474689_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474689
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474690_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474690_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474690
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474691_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474691_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474691
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474692_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474692_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474692
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474693_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474693_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474693
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474694_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474694_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474694
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474695_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474695_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474695
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474696_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474696_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474696
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474697_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474697_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474697
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474698_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474698_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474698
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474699_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474699_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474699
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474700_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474700_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474700
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474701_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474701_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474701
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474702_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474702_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474702
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474703_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474703_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474703
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474704_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474704_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474704
STAR —runThreadN 2 —genomeDir allna.fa --readFilesIn ~/Desktop/inf/term4python/pr/outs/ERR1474705_1.fastq, ~/Desktop/inf/term4python/pr/outs/ERR1474705_2.fastq --outFileNamePrefix ~/Desktop/inf/term4python/pr/mapped/ERR1474705

# htseq-count

<python script>

# DESeq2

# https://gist.github.com/wckdouglas/3f8fb27a3d7a1eb24c598aa04f70fb25

import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri, Formula
pandas2ri.activate()
from rpy2.robjects.packages import importr
deseq = importr('DESeq2')
'''
Adopted from: https://stackoverflow.com/questions/41821100/running-deseq2-through-rpy2
'''

to_dataframe = robjects.r('function(x) data.frame(x)')

class py_DESeq2:
    '''
    DESeq2 object through rpy2
    input:
    count_matrix: should be a pandas dataframe with each column as count, and a id column for gene id
        example:
        id    sampleA    sampleB
        geneA    5    1
        geneB    4    5
        geneC    1    2
    design_matrix: an design matrix in the form of pandas dataframe, see DESeq2 manual, samplenames as rownames
                treatment
    sampleA1        A
    sampleA2        A
    sampleB1        B
    sampleB2        B
    design_formula: see DESeq2 manual, example: "~ treatment""
    gene_column: column name of gene id columns, exmplae "id"
    '''
    def __init__(self, count_matrix, design_matrix, design_formula, gene_column='id'):
        try:
            assert gene_column in count_matrix.columns, 'Wrong gene id column name'
            gene_id = count_matrix[gene_column]
        except AttributeError:
            sys.exit('Wrong Pandas dataframe?')

        self.dds = None
        self.deseq_result = None
        self.resLFC = None
        self.comparison = None
        self.normalized_count_matrix = None
        self.gene_column = gene_column
        self.gene_id = count_matrix[self.gene_column]
        self.count_matrix = pandas2ri.py2ri(count_matrix.drop(gene_column,axis=1))
        self.design_matrix = pandas2ri.py2ri(design_matrix)
        self.design_formula = Formula(design_formula)


    def run_deseq(self, **kwargs):
        self.dds = deseq.DESeqDataSetFromMatrix(countData=self.count_matrix, 
                                        colData=self.design_matrix,
                                        design=self.design_formula)
        self.dds = deseq.DESeq(self.dds, **kwargs)
        self.normalized_count_matrix = deseq.counts(self.dds, normalized=True)

    def get_deseq_result(self, **kwargs):

        self.comparison = deseq.resultsNames(self.dds)

        self.deseq_result = deseq.results(self.dds, **kwargs)
        self.deseq_result = to_dataframe(self.deseq_result)
        self.deseq_result = pandas2ri.ri2py(self.deseq_result) ## back to pandas dataframe
        self.deseq_result[self.gene_column] = self.gene_id.values

# http://feb2014.archive.ensembl.org/Caenorhabditis_elegans/Location/Genome?ftype=DnaAlignFeature;id=MM454_FPK17YK01D0V75

# SAJR (http://storage.bioinf.fbb.msu.ru/~mazin/downloads.html)
# On the next step, we found out that the algorithm SAJR (for which we created files) works incorrectly. We initialized it a few times using different ways and, at least, the initialization was completed but the algorithm didn't work. I think the problem is in wrong file-pathways, as when I copied all files in parent dir the algorithm tried to work but gave wrong results


