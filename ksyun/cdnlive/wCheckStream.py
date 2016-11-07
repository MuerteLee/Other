#!/usr/bin/env python
# coding=utf-8
import os,sys
import argparse
import textwrap
import subprocess

def execute_cmdLine(cmdLine):
    p = subprocess.Popen(cmdLine, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE,shell=True);
    stdout,stderr = p.communicate()
    if p.returncode != 0:
        raise RuntimeError("%r failed, status code %s stdout %r stderr %r" % (cmdLine, p.returncode, stdout, stderr))
        return -1;
    return stdout;

def check_result(cmdLine):
    stdout=execute_cmdLine(cmdLine);
    std = stdout.split('\n')
    while '' in std:
        std.remove('');
    stdT = std[-1].strip('{').strip('}').strip("'").split(',')
    tResult = (stdT[-1].split(":")[-1].strip(''))
    if "True" == tResult.strip(' '):
        return 0;
    else:
        return -1;


if __name__ == "__main__":
    cmdLine = "python /Users/caijunli/Downloads/wStream/wCheckStream.py --check-time 5"
    parser = argparse.ArgumentParser(prog="autoCheckStream",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=textwrap.dedent('''python3 wCheckSteam.py -url url:'''),
                                 epilog="If any questions, please contact to licaijun@kingsoft.com")

    parser.add_argument('-u','--url',help='The args is url link.')
    parser.add_argument('-t','--type',help='The args is test type')
    parser.add_argument('-ip','--ip',help='The args is IP.')
    args = parser.parse_args()

    if args.ip:

        pass;
    if 'ffplay' in args.type:
        type = " -t ffplay"
    elif 'ffprobe' in args.type:
        type = " -t ffprobe"
    else:
        print("please check you type args!~")
        sys.exit(-1);

    if args.url: 
        urlTmp = args.url.split(':')
        if urlTmp[0] == "http":
            if "flv" in urlTmp[1] and 'hdllive' in urlTmp[1]:
                url = " -u " + args.url;
        elif urlTmp[0] == "rtmp" and 'rtmplive' in urlTmp[1]:
            if "flv" not in urlTmp[1]:
                url = " -u " + args.url;
        else:
            print("please check you url args!~")
            sys.exit(-1);
    cmdLine = cmdLine + url + type;
    if check_result(cmdLine) == 0:
        print("The %s status is success!~" %cmdLine)
        sys.exit(0);
    else:
        print("The %s status is failed!~" %cmdLine)
        sys.exit(-1)
