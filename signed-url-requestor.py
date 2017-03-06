#!/usr/bin/env python
"""
Generates signed URLs & makes corresponding requests to Requestor Pays buckets.

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
    --index-file        if set, script assumes you're download an index file
                        which should be parsed for urls of files to download
    -v                  verbose output for debugging
"""


import ConfigParser
import argparse
import os
import sys
from datetime import datetime
from pytz import timezone
import re
import base64
import hmac
import sha
import urllib2


def parse_args(argv):
    """Return the parsed arguments passed on the CLI."""
    # parse CLI arguments
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=("Signed URL generator for Requestor Pays S3 buckets\n"
                     "minimum requirements:\n"
                     "  - s3 file url\n"
                     "  - aws credentials "
                     "(as CLI arguments or in a credentials file)"))

    # read arguments passed to the script
    parser.add_argument('url',
                        help="url of the file to download from S3")
    parser.add_argument('--access-key',
                        help="your aws_access_key_id",
                        dest='access_key')
    parser.add_argument('--secret-key',
                        help="your aws_secret_access_key",
                        dest='secret_key')
    parser.add_argument('--aws-creds-file',
                        help=("path to aws credentials file, "
                              "defaults to ~/.boto"),
                        nargs='?',
                        default='~/.boto',
                        dest='aws_creds_file')
    parser.add_argument('--profile',
                        help=("profile/section within the "
                              "aws credentials file"),
                        dest='profile')
    parser.add_argument('--output-dir',
                        help=("the directory to save the requested file in, "
                              "defaults to current directory"),
                        nargs='?',
                        default='./',
                        dest='output_dir')
    parser.add_argument('--index-file',
                        action='count',
                        help=("if set, the script assumes the url represents "
                              "an index file. "
                              "The file downloaded will be read "
                              "to find additional urls to download"),
                        dest='index_file')
    parser.add_argument('-v', '--verbose',
                        action='count',
                        help="verbose output",
                        dest='verbose')
    args = parser.parse_args()
    return args


def parse_creds_file(path, taglist, profile):
    """Parse aws credentials file."""
    print "No API keys passed as CLI arguments, so checking credentials file"
    path = os.path.expanduser(path)
    if verbosity >= 1:
        print "Expanded path to aws credentials file: {}".format(path)

    if (os.path.isfile(path) is not True):
        print"AWS credentials file does not exist: {}".format(path)
        return False

    config = ConfigParser.SafeConfigParser()

    try:
        config.read(path)
    except:
        print"Cannot find aws credentials file: {}".format(path)
        return False

    if not profile:
        # we will look for a default/credentials profile
        if verbosity >= 1:
            print ("No profile specified on the CLI, "
                   "looking for a default/credentials profile ")
        if config.has_section("default"):
            profile = "default"
        elif config.has_section("Default"):
            profile = "Default"
        elif config.has_section("DEFAULT"):
            profile = "DEFAULT"
        elif config.has_section("credentials"):
            profile = "credentials"
        elif config.has_section("Credentials"):
            profile = "Credentials"
        elif config.has_section("CREDENTIALS"):
            profile = "CREDENTIALS"
        else:
            print("Cannot find a default or credentials profile "
                  "in your aws credentials file: {}".format(path))
            return False

    try:
        config.options(profile)
        if verbosity >= 1:
            print ("Found the {} profile "
                   "in your aws credentails file: {}".format(profile, path))
    except:
        print("Cannot find a section in the aws credentials file"
              "called: {}".format(profile))
        return False

    params = dict()
    for tag in taglist:
        if tag in config.options(profile):
            params.update({tag: config.get(profile, tag)})
        else:
            params.update({tag: None})
    return params


def dissect_s3url(url):
    """Return the s3 bucket & prefix."""
    # use regex to pull out the bucket & prefix
    re_start_s3 = re.compile('^s3://')
    re_start_http = re.compile('^https?://')

    re_s3 = re.compile(
        '^s3://([^/]+)(/.*?)$')
    re_http1 = re.compile(
        '^https?://([^.]+)[.]s3[.]amazonaws[.]com(/.*?)$')
    re_http2 = re.compile(
        '^https?://([^.]+)[.]s3-website-[^.]+[.]amazonaws.com(/.*?)$')
    re_http3 = re.compile(
        '^https?://s3[^.]+[.]amazonaws.com/([^/]+)(/.*?)$')

    if re_start_s3.match(url):
        s3_url = re_s3.match(url)
        (bucket, prefix) = (s3_url.group(1), s3_url.group(2))
        return (bucket, prefix)
    elif re_start_http.match(url):
        http_url_1 = re_http1.match(url)
        http_url_2 = re_http2.match(url)
        http_url_3 = re_http3.match(url)
        if http_url_1:
            (bucket, prefix) = (http_url_1.group(1), http_url_1.group(2))
            return (bucket, prefix)
        elif http_url_2:
            (bucket, prefix) = (http_url_2.group(1), http_url_2.group(2))
            return (bucket, prefix)
        elif http_url_3:
            (bucket, prefix) = (http_url_3.group(1), http_url_3.group(2))
            return (bucket, prefix)
        else:
            return False
    else:
        return False


def get_datetime():
    """Return the date in standard format, inc timezone."""
    gmt = timezone('GMT')
    dtnow = datetime.now()
    dtnow_loc = gmt.localize(dtnow)
    date = dtnow_loc.strftime("%a, %d %b %Y %X %Z")
    return date


def make_signature(bucket, prefix, aws_secret_key):
    """Return the bucket, prefix and signature."""
    # get the datetime
    date = get_datetime()

    string_to_sign = ("GET\n" +
                      "\n" +
                      "\n" +
                      date + "\n"
                      "x-amz-request-payer:requester\n" +
                      "/" + bucket + prefix)
    if verbosity >= 1:
        print "string_to_sign set to:\n{}".format(string_to_sign)

    h = hmac.new(aws_secret_key, string_to_sign, sha)
    signature = base64.encodestring(h.digest().strip())
    if verbosity >= 1:
        print "\nSignature calculated is: {}".format(signature.strip())
    return (bucket, prefix, signature)


def make_request(bucket, prefix, signature, aws_access_key):
    """Make the signed request, return the S3 object requested."""
    # construct the request for the signed url
    # including all necessary headers for a Requester Pays bucket

    if verbosity >= 1:
        print "Determined the bucket is: {}".format(bucket)
        print "Determined the prefix is: {}".format(prefix)

    # use urllib2 to build the request
    # first define the headers
    auth_header = "AWS " + aws_access_key + ":" + signature
    auth_header = auth_header.strip()
    if verbosity >= 1:
        print "Value of Authorization header is: {}".format(auth_header)
    date_header = get_datetime()

    headers = {"Authorization": auth_header,
               "Date": date_header,
               "x-amz-request-payer": "requester"}

    # construct the request
    url = "https://" + bucket + ".s3.amazonaws.com" + prefix
    req = urllib2.Request(url, None, headers)
    print "Created the signed URL request"
    if verbosity >= 1:
        print "\nThe signed URL request is:"
        print req.get_method(), req.get_full_url()
        print "with the HTTP headers set to:"
        for header in req.header_items():
            print header

    print "Executing the signed URL request"
    try:
        opener = urllib2.build_opener()
        response = opener.open(req, None, 10)
        return response
    except urllib2.HTTPError as error:
        print "Error encountered attempting to download S3 object:"
        print "Got HTTP response: {} {}".format(error.code, error.msg)
        if verbosity >= 1:
            print "\nResponse HTTP headers:\n{}".format(error.info())
        print "\nResponse body:\n{}".format(error.read())
        return False
    except urllib2.URLError as url_error:
        print ("Error encountered attempting to download "
               "S3 object:{}".format(url_error))
        return False


def download_file(bucket, prefix, aws_access_key, aws_secret_key, directory):
    """Sign & make request, save file returned."""
    # create the signature
    print ("\n========================\n"
           "Creating the signature to use in the request")
    try:
        (bucket, prefix, signature) = make_signature(bucket,
                                                     prefix,
                                                     aws_secret_key)
    except TypeError:
        print "Unable to complete signature creation"
        return False

    # now make the signed URL request
    response = make_request(bucket, prefix, signature, aws_access_key)

    if response is False:
        return False

    if verbosity >= 1:
        print "\nResponse summary:"
        print "request url:{}".format(response.url)
        print "status code:{}".format(response.code)
        print "msg:{}".format(response.msg)
        print "\nResponse HTTP headers:\n{}".format(response.info())

    print "\nDownloading: {}".format(response.url)

    # pick out the filename from the s3 prefix
    re_file = re.compile('.*/(.*?)$')
    filename = re_file.match(prefix).group(1)

    # ensure the output_dir ends with /
    output_dir = directory
    output_dir = os.path.abspath(output_dir)
    re_path = re.compile('.*/$')
    path = re_path.match(output_dir)
    if not path:
        output_dir = output_dir + "/"

    filepath = output_dir + filename

    # then write response object out to the filesystem
    try:
        with open(filepath, 'w') as output_file:
            output_file.write(response.read())
        return filepath
    except IOError as error:
        print ("Error writing s3 object to file: {}\n"
               "It's likely that the specified directory {} "
               "doesn't exist".format(filepath, output_dir))
        if verbosity >= 1:
            print "The full error is {}".format(error)
        return False


def main(argv):
    """Main function for the script, which calls everything else."""
    # use the AWS creds / conf file & S3 URL to construct the signed URL
    # then make the request
    # will use the Authorization header method to create the signed URL

    # make it clear that the user will pay for requests & downloads
    print ("You are about to download files from a "
           "'Requestor Pays' S3 bucket\n"
           "This means you will be charged for each request & download\n"
           "Further details of these costs can be found here:\n"
           "https://aws.amazon.com/s3/pricing/\n")

    resp = raw_input("Press any key to continue...\n")

    # parse CLI args passed to the script
    args = parse_args(argv)

    # set verbosity global variable so it can be used in all functions
    global verbosity
    verbosity = args.verbose

    # If aws keys aren't specified on the cli, read them from creds file
    key_tags = ['aws_access_key_id', 'aws_secret_access_key']
    if args.access_key is None or args.secret_key is None:
        try:
            params = parse_creds_file(args.aws_creds_file,
                                      key_tags,
                                      args.profile)
            args.access_key = params[key_tags[0]]
            args.secret_key = params[key_tags[1]]
        except TypeError:
            print ("Error encountered whilst attempting to "
                   "parse your AWS credentials file")
            return False
        if args.access_key is None or args.secret_key is None:
            print("Unable to get AWS API keys, "
                  "either specify them on the CLI "
                  "(--access-key, --secret-key), "
                  "or in a creds file (--aws-creds-file) "
                  "or ensure they are in ~/.boto")
            return False

    print "AWS API keys found"
    if verbosity >= 1:
        print "aws_access_key_id is {}".format(args.access_key)
        print "aws_secret_access_key is {}".format(args.secret_key)

    print "URL provided: {}".format(args.url)

    try:
        (bucket, prefix) = dissect_s3url(args.url)
    except TypeError:
        print (
            "URL not a supported S3 URL, "
            "please provide the S3 URL in one of these formats:\n"
            "s3://<bucket><prefix>\n"
            "http(s)://<bucket>.s3.amazonaws.com<prefix>\n"
            "http(s)://<bucket>.s3-website-eu-west-1.amazonaws.com<prefix>\n"
            "http(s)://s3-eu-west-1.amazonaws.com/<bucket><prefix>\n"
            "NB: <prefix> always starts with a /")

    filepath = download_file(bucket,
                             prefix,
                             args.access_key,
                             args.secret_key,
                             args.output_dir)
    if filepath is False:
        print "Error downloading & saving file, exiting"
        return False
    else:
        print ("Saved retrieved S3 object to: {}"
               "\n========================\n".format(filepath))

    # process index files
    # downloading all files within the index file
    if args.index_file:
        re_index = re.compile('.*index.txt$')
        index_prefix = re_index.match(prefix)
        if index_prefix:
            print "You provided a correctly named index file"
            # read the first line of the file, make sure it's an s3 url
            with open(filepath, 'r') as index_file:
                start_pos = index_file.tell()
                first_line = index_file.readline()
                try:
                    (bucket, prefix) = dissect_s3url(first_line)
                    print ("At an initial glance, index file looks good")
                except TypeError:
                    print ("First line of the index file is not an S3 URL\n"
                           "Please ensure the index file only contains "
                           " S3 URLs, "
                           "one per line")
                    return False
                # rewind the file to the start
                index_file.seek(start_pos)
                # count the no. of lines/urls in the file
                for index, line in enumerate(index_file):
                    pass
                line_count = index + 1
                # try to download all files listed in the file
                # after confirming the user really wants to
                resp = raw_input("You are about to download all files listed "
                                 "in {}\nWith one S3 URL per line, this "
                                 "represents {} files\n"
                                 "Are you sure you want to proceed? "
                                 "(Y/N): ".format(args.url, line_count))
                while True:
                    resp = resp.lower()
                    if resp == "y":
                        # rewind the file to the start again
                        index_file.seek(start_pos)
                        for line in index_file:
                            # Pull the bucket and prefix out of the S3 URL
                            (bucket, prefix) = dissect_s3url(line)
                            # sign & make request, download the file
                            filepath = download_file(bucket,
                                                     prefix,
                                                     args.access_key,
                                                     args.secret_key,
                                                     args.output_dir)
                            if filepath is False:
                                print ("Error downloading & saving file, "
                                       "exiting")
                                return False
                            else:
                                print ("Saved retrieved S3 object "
                                       "to: {}".format(filepath))
                                print "========================\n"
                        break
                    elif resp == "n":
                        print ("OK exiting without downloading all files "
                               "listed in {}".format(args.url))
                        return False
                        break
                    else:
                        resp = raw_input("Invalid response, "
                                         "please respond with Y/N: ")
        else:
            print ("Sorry the URL you provided {}"
                   " does not represent a correctly named index file.\n"
                   "Please ensure the file is named *.index.txt\n"
                   "and only contains S3 URLs of files to download, "
                   "one per line".format(args.url))
            return False


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print "\nYou pressed Ctrl+C so I quit"
