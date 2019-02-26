# The accuracy statistics quoted were derived by aligning to a derivative of the
# GRCh38 human genome release, modified by applying high confidence calls from
# NA12878 sample. This makefile serves as documentation for such a procedure.


FETCH := wget

.PHONY: all
all: na12878.maternal.fa na12878.paternal.fa na12878.vcf.gz na12878.reference.fa

#  Get variant calls:
na12878.vcf.gz: na12878.vcf.md5
	${FETCH} ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/release/NA12878_HG001/NISTv3.3.2/GRCh38/HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_PGandRTGphasetransfer.vcf.gz
	md5sum --ignore-missing --check $< && mv HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_PGandRTGphasetransfer.vcf.gz $@

na12878.vcf.md5:
	${FETCH} -O - ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/release/NA12878_HG001/NISTv3.3.2/GRCh38/md5sum \
	| tr -d '()'  \
	| awk 'BEGIN{OFS="  "}{print $$4, $$2}' > $@


#  Fix-up VCF -- drop unphased and sort out overlapping calls
%.fixed.vcf: %.vcf.gz
	zgrep '^#\|PATMAT' $< | vcfcreatemulti > $@


#  Get reference genome and fix up names
%.reference.fa:
	${FETCH} -O - ftp://ftp.ensembl.org/pub/release-90/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz \
	| gunzip \
	| sed 's/^>\([[:digit:]XY]\)/>chr\1/; s/^>MT/>chrM/' > $@

%.paternal.fa: %.reference.fa %.reference.fa.fai %.fixed.vcf.gz %.fixed.vcf.gz.tbi
	samtools faidx $*.reference.fa chr`seq -s ' chr' 1 22` chrX chrY chrM \
	| bcftools consensus --haplotype 1 $*.fixed.vcf.gz  \
	| sed 's/^\(>chr[[:alnum:]]\+\) .\+/\1_NA12878_paternal/' > $@

%.maternal.fa: %.reference.fa %.reference.fa.fai %.fixed.vcf.gz %.fixed.vcf.gz.tbi
	samtools faidx $*.reference.fa chr`seq -s ' chr' 1 22` chrX chrY chrM \
	| bcftools consensus --haplotype 2 $*.fixed.vcf.gz \
	| sed 's/^\(>chr[[:alnum:]]\+\) .\+/\1_NA12878_maternal/' > $@

# Compress and index VCF file
%.vcf.gz: %.vcf
	bgzip -i $<

# Create tabix file from vcf.gz
%.vcf.gz.tbi: %.vcf.gz
	tabix $<

# Index a FASTA file
%.fa.fai: %.fa
	samtools faidx $<

# Sort a BAM file
%.sort.bam: %.bam
	samtools sort $< $(basename $@)

# Index a BAM file
%.sort.bam.bai: %.sort.bam
	samtools index $<

%.mmi: %.fa
	minimap -d $@ $<

%.mmi2: %.fa
	minimap2 -d $@ $<

%.mmiH2: %.fa
	minimap2 -H -d $@ $<
