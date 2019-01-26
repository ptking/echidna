import sys
import os
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('-r','--run_monitor_id',required=True)

args = parser.parse_args()

print("Running Workflow...")


print("Run Monitor Id: " + str(args.run_monitor_id))

print("Done")
