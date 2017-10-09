# ONT-HG1

2017-10: ONT-HG1 (Cliveome2) rebasecalled data from 2017-05.
2017-05: ONT-HG1 (Cliveome2) GridION data release 2017-05. Two GridION runs were performed. Basecalling was performed using a pre-production transducer model implemented in scrappie (now available in production basecallers); basecalls therefore do not contain quality scores.

## Index

* [BAMs](#bams)
* [Indices](#indices)
* [Fast5s](#fast5s)
* [23andMe SNPs](#23-and-me-snps)

## BAMs ##

| Date    | Size | File                                                                                  | Description | MD5                              |
|---------|------|---------------------------------------------------------------------------------------|-------------|----------------------------------|
| 2016-10 | 130G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/merge_sort/cliveome2.bam) | merged      | d80e3620e0cf6fa97b2cb61ec507eabc |
| 2016-10 | 9.6G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr1.bam)          | Chr1        | 0fd4438c83648746a306544977c9d53a |
| 2016-10 | 11G  | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr2.bam)          | Chr2        | a32ca31a172259b199953b0e8bc37fcd |
| 2016-10 | 8.3G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr3.bam)          | Chr3        | 2204c24a622207be8526588ee1ea118b |
| 2016-10 | 8.7G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr4.bam)          | Chr4        | 7a9872783640b506f19d382343e3742f |
| 2016-10 | 7.6G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr5.bam)          | Chr5        | b8348ad5581f9cc4b056e1304c03d5a5 |
| 2016-10 | 7.3G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr6.bam)          | Chr6        | 7944b310b73acc9765c0450c65a7f5b6 |
| 2016-10 | 6.8G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr7.bam)          | Chr7        | 9c53c3ac83aa40b9e9530d3c0395919d |
| 2016-10 | 6.4G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr8.bam)          | Chr8        | e3a901cd523e403de2cc7cdfb8e887e7 |
| 2016-10 | 5.1G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr9.bam)          | Chr9        | 1acf365933799e7ed8259a9566ed6c48 |
| 2016-10 | 7.0G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr10.bam)         | Chr10       | d3d5499202ded1ce9adadaa2acec3b0c |
| 2016-10 | 5.6G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr11.bam)         | Chr11       | e38f95d049b1a31adf758a202a5e2e83 |
| 2016-10 | 5.6G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr12.bam)         | Chr12       | d0e519aea2afd44588c0b9ce41b8df09 |
| 2016-10 | 4.2G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr13.bam)         | Chr13       | 3b6395310c76debb33b62c3617a1a817 |
| 2016-10 | 3.8G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr14.bam)         | Chr14       | cbe2891b31936faec37f85e13c2e21d0 |
| 2016-10 | 3.4G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr15.bam)         | Chr15       | f41c90a9218dee39c21f3017c7577224 |
| 2016-10 | 3.6G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr16.bam)         | Chr16       | 2c5993605a24d50a7f23c9c997cdf29c |
| 2016-10 | 3.3G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr17.bam)         | Chr17       | d7b369aa2389ff43ba60933760df73c1 |
| 2016-10 | 3.3G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr18.bam)         | Chr18       | 55f7e906363ea4738bc1f69d42ad17d3 |
| 2016-10 | 2.5G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr19.bam)         | Chr19       | 0c007c5a5ea9b4be353d6264d5e9b98b |
| 2016-10 | 2.5G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr20.bam)         | Chr20       | 14728d4e54fcc489e81dd4935cee09f1 |
| 2016-10 | 1.7G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr21.bam)         | Chr21       | 8e0f9f2b063f3ee47486d80ff7d15319 |
| 2016-10 | 1.6G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr22.bam)         | Chr22       | 011feb160c0b4bda8b89f91ff2706376 |
| 2016-10 | 3.4G | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chrX.bam)          | ChrX        | d3457a210f5dbcedf3d2b1814e29c8d7 |
| 2016-10 | 948M | [BAM](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chrY.bam)          | ChrY        | 952b93a64cd04f0aa2fe089abddc40e8 |



## Indices ##
| Date    | Size | File                                                                                      | Description | MD5                              |
|---------|------|-------------------------------------------------------------------------------------------|-------------|----------------------------------|
| 2016-10 | 1.1G | [TXT](https://s3-eu-west-1.amazonaws.com/ont-hg1b/basecalling_summary.txt.gz)             | Guppy basecalling_summary.txt.gz  | 9eb4b22b7c5fd7dc410bf33db1027cef |
| 2016-10 | 49M  | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/merge_sort/cliveome2.bam.bai) | merged      | d80e3620e0cf6fa97b2cb61ec507eabc |
| 2016-10 | 3.9M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr1.bam.bai)          | Chr1        | 95859b0eac10349270dc91d8b2a11e99 |
| 2016-10 | 4.4M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr2.bam.bai)          | Chr2        | 6bad5cfe938778250e35270ed5a033e7 |
| 2016-10 | 3.5M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr3.bam.bai)          | Chr3        | 10194175ece7f20cd848799f0ea03e35 |
| 2016-10 | 3.6M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr4.bam.bai)          | Chr4        | c07aae35c0b2c1a357c56e080316af62 |
| 2016-10 | 3.2M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr5.bam.bai)          | Chr5        | ce494e9ee932a80aa94616207e5a8dc6 |
| 2016-10 | 3.0M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr6.bam.bai)          | Chr6        | 38fc20209f7fc06f81ae3a2e9c5cde9c |
| 2016-10 | 2.8M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr7.bam.bai)          | Chr7        | 485924ab264e33f15bfdd13e190b3264 |
| 2016-10 | 2.6M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr8.bam.bai)          | Chr8        | fb8062e233eef1b3647148c7fd34fa83 |
| 2016-10 | 2.1M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr9.bam.bai)          | Chr9        | 356019b3761502ded684ea2a6c3ca1bc |
| 2016-10 | 2.5M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr10.bam.bai)         | Chr10       | 9b582b402782c8be1229a78fd600391b |
| 2016-10 | 2.3M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr11.bam.bai)         | Chr11       | 6a7dfd7805eca7af43a1e32e74af3c8f |
| 2016-10 | 2.3M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr12.bam.bai)         | Chr12       | e0f3052b106caeb1d957e47ff2523b7b |
| 2016-10 | 1.7M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr13.bam.bai)         | Chr13       | 5b506984df5606b329df41ecc5348203 |
| 2016-10 | 1.6M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr14.bam.bai)         | Chr14       | 0c0e0019b40afeb0aff6d326826db29a |
| 2016-10 | 1.5M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr15.bam.bai)         | Chr15       | 5d25fdbc2580cecee3e20c75349ad370 |
| 2016-10 | 1.5M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr16.bam.bai)         | Chr16       | 84a1a295d8e8cf468e8715b4849c21b4 |
| 2016-10 | 1.3M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr17.bam.bai)         | Chr17       | 6ff30bc38696fb63556653153ff27e2d |
| 2016-10 | 1.4M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr18.bam.bai)         | Chr18       | 31b6071d1cfb4beda3b510044580700c |
| 2016-10 | 1.1M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr19.bam.bai)         | Chr19       | 7a28abed3be88e00b5d54e393df0e9c5 |
| 2016-10 | 1.0M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr20.bam.bai)         | Chr20       | ec9ed04df3d2e336e505eb686c96a34a |
| 2016-10 | 679K | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr21.bam.bai)         | Chr21       | 1a75e5a1bbff059ff90b232fde36357f |
| 2016-10 | 574K | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chr22.bam.bai)         | Chr22       | 9adf6e4e25d152a846f20b233e74ac59 |
| 2016-10 | 1.6M | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chrX.bam.bai)          | ChrX        | d27ff8e92b93c9fba7dde25336b4cbb6 |
| 2016-10 | 390K | [BAI](https://s3-eu-west-1.amazonaws.com/ont-hg1b/alignment/by_chr/chrY.bam.bai)          | ChrY        | 663d6e3795f3459c777dd79c1415e69e |

## Fast5s ##

| Date    | Size | Indices                                                                   | MD5                              |
|---------|------|---------------------------------------------------------------------------|----------------------------------|
| 2016-05 | 116M | [Fast5](https://s3-eu-west-1.amazonaws.com/ont-hg1b/fast5-listing.txt.gz) | d80e3620e0cf6fa97b2cb61ec507eabc |

* To download fast5s, fetch each URL from the file listing above, using e.g. wget -i fast5-listing.txt.gz

## 23 and Me SNPs ##

| Name         | Size | Links                                                                                                        | MD5                              |
|--------------|------|--------------------------------------------------------------------------------------------------------------|----------------------------------|
| 23andMe SNPs | 5M   | [SNPs](https://s3-eu-west-1.amazonaws.com/ont-hg1b/23andMe/genome_Clive_Brown_v2_Full_20171006051504.txt.gz) | 6c7464d34dfc3f6d31439eaaf823a344 |
