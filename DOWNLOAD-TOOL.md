# signed-url-requestor.py

This tool is intended to make downloading ONT-HG1 files easy.

We host the ONT-HG1 files on AWS S3 (Simple Storage Service) and have turned on the 'Requestor Pays' feature; this means the cost of your file downloads are passed onto you, specfically the cost of the request and the data transfer. Details of S3 request and data transfer costs can be found here: https://aws.amazon.com/s3/pricing/

To download objects from a Requestor Pays S3 bucket you have to 'sign' your requests, using your AWS API keys. This tool (script) takes care of that.

In summary to download the ONT-HG1 files you need: 

- an AWS account, with API keys
- your AWS account must have a role assigned to it (any role will suffice)
- use the signed-url-requestor.py script as described below to complete the download


### Download the script

The script can be downloaded from [here](signed-url-requestor.py) 
   

### Prerequisites

The script is written in Python, specifically Python 2 syntax, so ensure Python 2.x is installed, you can download it from here: https://www.python.org/downloads/

The script has been tested on Python 2.7.10, running on Mac OS X 10.11.6


### Using the script

At the command line execute:

	python signed-url-requestor.py <url> [OPTIONAL ARGUMENTS]

For example:

	python signed-url-requestor.py http://ont-hg1.s3-website-eu-west-1.amazonaws.com/fastq/FAB48453.merged.fq.gz --output-dir downloads/

If you want help understanding how to run the script pass the `-h` or `--help` arguments to the script:

	python signed-url-requestor.py --help

Compulsory arguments:

    url               the url of the file to download from S3

    Your AWS API keys, by supplying either:

    --access-key        your API access key
    --secret-key        your API secret key
    
    or:
    
    --aws-creds-file    aws credentials file, formatted like a boto creds file
                        will default to ~/.boto

Optional arguments:

    --profile           the section within your aws credentails file to use
    --output-dir        the directory to save the downloaded file in
    --index-file        if set, the script assumes you're downloading an index file
                        which should be parsed for urls of files to download
    -v                  verbose output for debugging
