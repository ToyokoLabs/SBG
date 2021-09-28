import subprocess
import time
import logging
import os

import boto3


bucket_dir = 'gs://sbglabdata/4pep'
logging.basicConfig(filename='runamber.log', filemode='a',
                    level=logging.INFO)
tleap_template = """source leaprc.ff14SB
peptide = sequence {}
saveAmberParm peptide p.1.top p.1.crd
quit"""
awskeys = open('keys.csv').read()
keyid, secret = awskeys.split(',')
client = boto3.resource('sqs', region_name='us-west-2',
                    aws_access_key_id=keyid, 
                    aws_secret_access_key=secret[:-1])
qname = 'pep4aa-r1'
replic_number = qname[-1]
sqs_q = 'https://sqs.us-west-2.amazonaws.com/344265375347/' + qname

queue = client.get_queue_by_name(QueueName=qname)


def run_all(pepname):
    """

    """
    step1 = ('tleap', '-s', '-f', 'tleap.in')
    step2 = ('sander', '-O', '-i', 'min.1.in', '-o', 'min.1.out', 
            '-p', 'p.1.top', '-c', 'p.1.crd', '-r', 'min.1.crd')
    step3 = ('sander', '-O', '-i', 'dmd.1.inp', '-o', 
            '{}-R{}.dmd.1.out'.format(pepname, replic_number),
            '-p', 'p.1.top', '-c', 'min.1.crd', '-r', 
            '{}-R{}.prod.1.crd'.format(pepname, replic_number), '-x', 
            '{}-R{}.dmd.1.traj'.format(pepname, replic_number))
    subprocess.run(step1)
    time.sleep(.3)
    stp2 = subprocess.run(step2, capture_output=True)
    if stp2.stderr:
        logging.info('error in stp2')
        logging.info(stp2.stderr)
    time.sleep(.3)
    logging.info("Running ...{}".format(pepname))
    stp3 = subprocess.run(step3, capture_output=True)
    if stp3.stderr:
        logging.info('error in stp3')
        logging.info(stp3.stderr)


while True:
    retries = 10
    while retries:
        retries -= 1
        msg = queue.receive_messages(
                    QueueUrl=sqs_q,
                    MaxNumberOfMessages=1,
                    MessageAttributeNames=['All']
                    )
        if msg:
            break
        logging.info('sleeping before retrying...')
        time.sleep(60)        
    if not msg:
        logging.info('Empty queue')
        break
    new_pep = msg[0].body
    tleap = tleap_template.format(new_pep)
    with open('tleap.in', 'w') as tleapfh:
        tleapfh.write(tleap)
    pepname = new_pep.replace(' ', '')[1:-1]
    run_all(pepname)
    pepname = '{}-R{}'.format(pepname, replic_number)
    # Compress after running
    comp = 'tar -cjf {}.tar.bz2 p.1.top {}.dmd.1.out {}.dmd.1.traj {}.prod.1.crd'.format(
            pepname, pepname, pepname, pepname)
    subprocess.run(comp, shell=True).check_returncode()
    # Delete after compress
    delall = 'rm {}.dmd.1.out {}.dmd.1.traj {}.prod.1.crd'.format(
            pepname, pepname, pepname)
    subprocess.run(delall, shell=True).check_returncode()
    # upload that file
    upload_cmd = 'gsutil cp {}.tar.bz2 {}'.format(pepname, bucket_dir)
    subprocess.run(upload_cmd, shell=True).check_returncode()
    # Delete uploaded file
    rm_cmd = 'rm {}.tar.bz2'.format(pepname)
    subprocess.run(rm_cmd, shell=True).check_returncode()
    # Delete from queue
    queue.delete_messages(
            Entries=[{'Id': msg[0].message_id,
                    'ReceiptHandle': msg[0].receipt_handle}])
logging.info("Done")
