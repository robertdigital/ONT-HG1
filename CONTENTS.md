# ONT-HG1
ONT-HG1 (Cliveome) GridION data release 2017-05. Two GridION runs were performed. Basecalling was performed using a pre-production transducer model implemented in scrappie (now available in production basecallers); basecalls therefore do not contain quality scores.

## Index
* [Fast5s](#fast5s)
* [23andMe SNPs](#23-and-me-snps)

## Data

| Date    | Size | Indices                                                                   | MD5                              |
|---------|------|---------------------------------------------------------------------------|----------------------------------|
| 2016-05 | 116M | [Fast5](https://s3-eu-west-1.amazonaws.com/ont-hg1b/fast5-listing.txt.gz) | d80e3620e0cf6fa97b2cb61ec507eabc |
| 2016-05 |  16K | [Fasta](https://s3-eu-west-1.amazonaws.com/ont-hg1b/fasta_listing.txt)    | 85321855d9c33c96862663a3f588a1c9 |

Each gzipped .fasta file contains approximately 100k reads, in no particular order.

## 23 and Me SNPs

In order to download the files listed here, you will need to use our [Download Tool](DOWNLOAD-TOOL.md)

| Name         | Size | Links                                                                                                                   | MD5                              |
|--------------|------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 23andMe SNPs | 5M   | [SNPs](http://ont-hg1.s3-website-eu-west-1.amazonaws.com/snps-23andMe/genome_Clive_Brown_v2_Full_20161123020445.txt.gz) | 5df03968e7b7d97a21de336bfdab5700 |
