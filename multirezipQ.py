#!/usr/bin/env python3

import subprocess
import logging
from os import listdir
from os.path import isfile, join

import boto3

REPN = 3
TMPDIRNAME = 'tmpdir'
MAXBATCH = 5000


logging.basicConfig(filename='runmultirezipQ.log', filemode='a',
                    level=logging.INFO)

qname = 'rezipq'
sqs_q = 'https://sqs.us-west-2.amazonaws.com/344265375347/' + qname
# queue = client.get_queue_by_name(QueueName=qname)

awskeys = open('keys.csv').read()
keyid, secret = awskeys.split(',')

c2 = boto3.client('sqs', region_name='us-west-2',
                    aws_access_key_id=keyid,
                    aws_secret_access_key=secret[:-1])

while True:
    retries = 10
    while retries:
        retries -= 1
        msg = c2.receive_message(
            QueueUrl=sqs_q,
            MessageAttributeNames=[
                'All'
            ],
        )
        if msg:
            break
        logging.info('sleeping before retrying...')
        time.sleep(60)
    if not msg:
        logging.info('Empty queue')
        break
    pkg = msg['Messages'][0]['Body']
    md5 = msg['Messages'][0]['MD5OfBody']
    logging.info('Doing msg: {}'.format(md5))
    for p in pkg.split('/'):
        f = 'N{}-R{}.tar.bz2'.format(p, REPN)
        # Download file
        cmd = 'gsutil cp gs://sbglabdata/5pep/{} {}/'.format(f,
                TMPDIRNAME)
        subprocess.run(cmd, shell=True).check_returncode()
        # Uncompress
        cmd = 'bzip2 -dc {}/{} > {}/{}'.format(
                    TMPDIRNAME, f, TMPDIRNAME, f[:-4])
        subprocess.run(cmd, shell=True).check_returncode()
        # delete bzip2 file
        cmd = 'rm {}/{}'.format(TMPDIRNAME, f)
        subprocess.run(cmd, shell=True).check_returncode()
        # untar
        cmd = 'tar -xf {}/{} -C {}'.format(
                    TMPDIRNAME, f[:-4] , TMPDIRNAME)
        subprocess.run(cmd, shell=True).check_returncode()
        # delete tars
        cmd = 'rm {}/*.tar'.format(TMPDIRNAME)
        subprocess.run(cmd, shell=True).check_returncode()
        # rename top file
        cmd = 'mv {}/p.1.top {}/N{}-R{}.1.top'.format(TMPDIRNAME,
                   TMPDIRNAME, p, REPN)
        subprocess.run(cmd, shell=True).check_returncode()
    # make big tar
    arch_name = '{}-R{}.tar'.format(md5, REPN)
    cmd = 'tar -cvf {} {}/'.format(arch_name, TMPDIRNAME)
    subprocess.run(cmd, shell=True).check_returncode()
    # compress xz
    cmd = 'xz -z9 {}'.format(arch_name)
    subprocess.run(cmd, shell=True).check_returncode()
    # Delete all structures files
    cmd = 'rm {}/*'.format(TMPDIRNAME)
    subprocess.run(cmd, shell=True).check_returncode()
    # Delete msg
    c2.delete_message(
        QueueUrl = sqs_q,
        ReceiptHandle = msg['Messages'][0]['ReceiptHandle']
    )
    logging.info('msg deleted')
