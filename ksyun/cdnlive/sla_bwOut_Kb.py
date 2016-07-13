#!/usr/bin/env python
# coding=utf-8
import os
tmpBwOut=[]
def CalculateDiff(value1, value2, value3, rightInfo, errorInfo, tmpList):
    if abs(value1 - value2) == value3:
        print(rightInfo)
    elif  abs(value1 - value2) > value3:
        if  abs(value1 - value2) == value3-1:
            print(rightInfo)
    else:
        print(errorInfo,tmpList)

    if value3 == abs(int(tmpList[12])) or value3 == abs(int(tmpList[9])):
        if value3 > 3000:
            print("the diff value3 is big than 3000", errorInfo,tmpList)




def findError(pathFile):
    NULLVALUE = 0
    NULLVALUEG = []
    with open (pathFile) as f:
        lines = f.readlines();
        for (num,line) in enumerate(lines):
            if "pull_av_bw" in line and "relay_pull_av_bw" not in line:
                tmpBwOut = line.strip('\n').split("\t")[18:]
                CalculateDiff(abs(int(tmpBwOut[2])),abs(int(tmpBwOut[0])),abs(int(tmpBwOut[3])),"successful->bw_out_diff_kb","Failed->bw_out_diff_kb",tmpBwOut)
                CalculateDiff(abs(int(tmpBwOut[5])),abs(int(tmpBwOut[4])),abs(int(tmpBwOut[6])),"successful->last_av_ts_diff","Failed->last_av_ts_diff",tmpBwOut)
                CalculateDiff(abs(int(tmpBwOut[8])),abs(int(tmpBwOut[7])),abs(int(tmpBwOut[9])),"successful->audio_ts_diff","Failed->audio_ts_diff",tmpBwOut)
                CalculateDiff(abs(int(tmpBwOut[11])),abs(int(tmpBwOut[10])),abs(int(tmpBwOut[12])),"successful->video_ts_diff","Failed->video_ts_diff",tmpBwOut)

                #print(tmpBwOut)
    f.close();


if __name__ == "__main__":
    cmdLTmp = "/home/licaijun/access.log"
    findError(cmdLTmp)
