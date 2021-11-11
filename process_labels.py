import xml.etree.ElementTree as ET
import os
import cv2

def process_labels():

    in_file = open("/home/cse-305/xwq_files/dataset/safety_halmet_dateset/test64.txt")
    # label_id = label_id.replace('.txt', '')
    out_file = open("/home/cse-305/xwq_files/dataset/safety_halmet_dateset/test64_yolov3.txt", 'w')
    for line in in_file:
        line = line.replace('./', '')
        out_file.write('/home/cse-305/xwq_files/dataset/safety_halmet_dateset/' + line)


if __name__ == '__main__':
    process_labels()