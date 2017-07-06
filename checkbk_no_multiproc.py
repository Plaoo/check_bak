import datetime
import glob
import os
import subprocess
import re
import datetime
import smtplib
from email.mime.text import MIMEText
import time

pathlist = os.curdir


def send_mail(log):
    fp = open(log, "r")

    msg = MIMEText(fp.read())
    msg['Subject'] = 'Backup corrotti'
    msg['From'] = 'cloudbackup-alert@betatechnologies.com'
    msg['To'] = 'paolo.monni345@gmail.com'

    s = smtplib.SMTP("mail.betatechnologies.com", 25)  # server smtp
    s.send_message(msg)
    s.quit()


def check(filename, log):
    # path7zip = "C:\Program Files\\7-Zip\\7z.exe"
    path7zip = "/usr/bin/7z"
    command = [path7zip, 't', filename]
    sp = subprocess.Popen(command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    out = str(sp.communicate())
    out = out.replace("\\n", "\n").replace("\\r", " ").replace("\\\\", "\\")
    for line in out.splitlines():
        if re.search('^ERROR:', line):
            with open(log, 'a') as writee:
                writee.write("{0} {1}\n".format(os.path.abspath(filename), line))


if __name__ == "__main__":
    start = time.time()
    log = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt"

    for root, subdirs, files in os.walk(pathlist):
        for names in files:
            fname = os.path.join(root, names)
            if fname.endswith(".zip"):  # or fname.endswith(".rar") or fname.endswith(".7z"):
                check(fname, log)
                # if os.path.isfile(log):
                #    send_mail(log)
    print("Time taken = {0:.5f}".format(time.time() - start))
