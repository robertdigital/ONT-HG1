
Version 3.0
-----------

We're happy to announce the release of a new Cliveome data set released in February 2019.
This is the first update since October 2017 and now incorporates all the platform updates that have occurred in the last 14 months.
The data set contains ~80X coverage of Cliveome generated from 3 PromethION flow cells.

Key stats:
 * 240 Gb called
 * Read N50 for these runs combined are ~57 kb

Version Management:
 * Device: PromethION Beta
 * Flow Cell: FLO-PRO002 (R9.4.1)
 * PromethION Software Version: 19.01
 * Firmware version: 0.10 - includes the fix for device temperature
 * Basecalling: Flip-Flop Model in Guppy 2.3.5

Further details on data generation methods are available to member of the Nanopore Community:
https://community.nanoporetech.com/posts/cliveome-v3-r9-4-1-feb19


**Data**

The data added in version 3.0 can be accessed from AWS S3 at the following prefixes

| Dataset | Size  | Prefix                                             | File listing                                                                                               | Checksums                                                                                               |
|---------|-------|----------------------------------------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| .fastq  | 800Gb | "s3://ont-hg1b/PromethION CliveOME_2019-02/fastq/" | [fastq.listing.txt](https://s3-eu-west-1.amazonaws.com/ont-hg1b/PromethION+CliveOME_2019-02/fastq/fastq.listing.txt) | [fastq.md5sums.txt](https://s3-eu-west-1.amazonaws.com/ont-hg1b/PromethION+CliveOME_2019-02/fastq/fastq.md5sums.txt) |
| .fast5  | 4Tb   | "s3://ont-hg1b/PromethION CliveOME_2019-02/fast5/" | [fast5.listing.txt](https://s3-eu-west-1.amazonaws.com/ont-hg1b/PromethION+CliveOME_2019-02/fast5/fast5.listing.txt) | [fast5.md5sums.txt](https://s3-eu-west-1.amazonaws.com/ont-hg1b/PromethION+CliveOME_2019-02/fast5/fast5.md5sums.txt) |



Version 2.1
-----------

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1318628.svg)](https://doi.org/10.5281/zenodo.1318628)

*Updated 9 Oct 2017*

*See [CONTENTS.ver2.md](https://github.com/nanoporetech/ONT-HG1/blob/master/ver2/CONTENTS.md)*

The original cliveome data from the two later GridION runs has been recalled (by Chris Wright) using Guppy (0.2.3) which was the latest version at the time of writing. The 23andMe SNP calls file has also been updated (so much for 'gold standard' genotyping).

All other terms and condition as per the original README and License below.


c.


Version 2.0
-----------

*Updated 26 Jun 2017*

Below is the original ReadMe from our first attempt at a self-sequenced human genome on nanopore technology (cliveome). Some months ago we re-ran using fresh blood, but this time on GridION. Per flowcell yields were between 12 and 14Gbases and more recently we are seeing customer runs on MinION matching or exceeding these. As of 26th Jun 2017 we should start to see comparable GridION runs in field. We've posted these new data in the week when we are about to do another cliveome run from fresh blood, this time using some of the 'ultra-long' read preparations that have been shown elsewhere.

These data are additive. The file sizes are large, so after a few weeks we will have a 'user-pays' system that covers the amazon cloud download fees.

I performed the steps, and most importantly ran the apparatus (camera), so the Copyright notices and license assertions from the original cliveome are applicable to these newer datasets.

enjoy

c.


This Genome is a Work In Progress
---------------------------------

So far as I am aware this is the first full coverage Human Genome sequenced by the individual who provided the input sample (ONT-HG1). This may prove significant in future. 

All other Human Genome sequencing to date has been provided as a service by a third party laboratory.

This is by no means the first named individual Human Genome sequence, previously others have been made available such as those from J. Craig Venter and James Watson albeit using different and older technologies.

As you can see from the [License](LICENSE.ver1-2.md), I am asserting Copyrights over this genome. I have included, briefly, some rationales for that claim. I believe they are valid, in any case, Copyrights should be explicitly extended to self-sequencing and publication.

Part of my motivation for sequencing myself and making the data public, under asserted rights, is to get the ball rolling on a new self-sequencing model. In the near future you will be able to take spittle, say, at home and sequence yourself on a regular basis. Data can be stored, analysed and tracked online under your control. If you also believe in this, I enjoin you to sequence yourselves at home and share your data (or not) under suitable rights of your choosing.

Its not widely understood outside of the genomics community that genomes are generally incomplete. Bits are missing or not accessible to certain technologies. Much genomic data is still based on comparison to a flawed reference genome, modifications are often not present, nor are tissue specific mutations/modifications - being averaged over. Using long read technologies such as Nanopore we can start to 'assemble' a genome from its parts. Such assembled genomes can be more complete. Arguably with reads beyond 7 Megabases, entire chromosomes can be assembled in one piece, preserving inherited patterns of mutations. That day is coming. Long read technologies can also detect modified bases, often overlooked (due to non-detection?) in historical genome sequencing.

Therefore, I am not going to pretend the genome here is fully finished or complete. But, I do think it is of comparable completeness to other published personal genomes. Work remains, particularly on base calling. Our existing base callers do not fully decode the underlying raw signals. As further advances are made, better versions of these data may be generated, so dealing with gaps and errors in the consensus. In particular the genome here was sequenced without PCR. The base callers are generally trained on PCR'd data. This means modified bases are likely to show up here as so-called 'systematic error' in the averaged consensus.

Another work around we may use is to retrain the base caller to map all signals, including modified bases, back to four base reference sequence (A,C,G,T). That data will also be deposited here.

We have only made a draft consensus assembly. That is WIP and looks very promising. That will be added to this site when ready.

The genome here was extracted from white blood cells. A particular interest is to look at the hyper-mutable regions of these cells that respond to disease or infection in order to generate antibodies. These regions can change over time and in future we aim to add time coursed 'immuno-profiling' to the data set.

We believe we have full coverage, with average ~50X. Thin patches can be added to as we attempt to assemble the consensus. On this site you will find files extracted from raw nanopore data, and links to the raw + basecalled files totalling about 40TB. When newer base callers have been run, the FastQs are likely to be replaced and superceded. You can also see how much data we got per flowcell, however, we did not run all flowcells for the full 48hrs, often we stopped runs early to swap to new flowcells.

Publishing these data is a starting point more than an end point. You might argue its only very symbolic as a lone genome. It's entirely possible nobody other than me ever looks at it in any detail and that it is over taken by newer data very quickly. That's all fine - buts it is mine to do with as I please.

Clive G. Brown
12 Dec 2016.
