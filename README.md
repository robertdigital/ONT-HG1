ReadMe
======

So far as I am aware this is the first full coverage Human Genome sequenced by the individual who provided the input sample (ONT-HG1). This may prove significant in future. 

All other Human Genome sequencing to date has been provided as a service by a third party laboratory.

This is by no means the first named individual Human Genome sequence, previously others have been made available such as those from J. Craig Venter and James Watson albeit using different and older technologies.

As you can see from the License, I am asserting Copyrights over this genome. I have included, briefly, some rationales for that claim. I believe they are valid, in any case, Copyrights should be explicitly extended to self-sequencing and publication.
	

Part of my motivation for sequencing myself and making the data public, under asserted rights, is to get the ball rolling on a new self-sequencing model. In the near future you will be able to take spittle, say, at home and sequence yourself on a regular basis. Data can be stored, analysed and tracked online under your control. If you also believe in this, I enjoin you to sequence yourselves at home and share your data (or not) under suitable rights of your choosing.

This Genome is (Work In Progress) WIP
=====================================

Its not widely understood outside of the genomics community that genomes are generally incomplete. Bits are missing or not accessible to certain technologies. Much genomic data is still based on comparison to a flawed reference genome, modifications are often not present, nor are tissue specific mutations/modifications - being averaged over. Using long read technologies such as Nanopore we can start to 'assemble' a genome from its parts. Such assembled genomes can be more complete. Arguably with reads beyond 7 Megabases, entire chromosomes can be assembled in one piece, preserving inherited patterns of mutations. That day is coming. Long read technologies can also detect modified bases, often overlooked (due to non-detection?) in historical genome sequencing.

Therefore, I am not going to pretend the genome here is fully finished or complete. But, I do think it is of comparable completeness to other published personal genomes. Work remains, particularly on base calling. Our existing base callers do not fully decode the underlying raw signals. As further advances are made, better versions of these data may be generated, so dealing with gaps and errors in the consensus. In particular the genome here was sequenced without PCR. The base callers are generally trained on PCR'd data. This means modified bases are likely to show up here as so-called 'systematic error' in the averaged consensus.

Another work around we may use is to retrain the base caller to map all signals, including modified bases, back to four base reference sequence (A,C,G,T). That data will also be deposited here.

We have only made a draft consensus assembly. That is WIP and looks very promising. That will be added to this site when ready.

The genome here was extracted from white blood cells. A particular interest is to look at the hyper-mutable regions of these cells that respond to disease or infection in order to generate antibodies. These regions can change over time and in future we aim to add time coursed 'immuno-profiling' to the data set.

We believe we have full coverage, with average ~50X. Thin patches can be added to as we attempt to assemble the consensus. On this site you will find FastQ files extracted from raw nanopore data, and links to the raw + basecalled Fast5 files totalling about 40TB. When newer base callers have been run, the FastQs are likely to be replaced and superceded. You can also see how much data we got per flowcell, however, we did not run all flowcells for the full 48hrs, often we stopped runs early to swap to new flowcells.

Publishing these data is a starting point more than an end point. You might argue its only very symbolic as a lone genome. It's entirely possible nobody other than me ever looks at it in any detail and that it is over taken by newer data very quickly. That's all fine - buts it is mine to do with as I please.

Clive G. Brown
12 Dec 2016.
