#!/usr/bin/env python3
""" This is a docstring """

from csv import reader
import os
import unittest
from random import randrange
from robotics.controllers.pid import PID
from util.num_help import clamp
from util.reports import plot_results

class test_robotics_pid(unittest.TestCase):
    print(F"Current working dir is {os.getcwd()}")

    # read csv file as a list of lists
    def get_data(self,csvfile):
        with open(csvfile, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            rows = [[float(row[0])] for row in csv_reader if row]
            # Pass reader object to list() to get a list of lists
            print(rows)
        data=[]        
        for i in rows:
            data.append(i[0])
        return data

    #Run a test of the PID
    def test_pid(self):
        pid = PID(0,.05,.03,1,1)
        pid_out=[] 
        data = self.get_data('tests/gyro.csv')
        self.assertTrue(data)
        print("data: ",data)
        for i in data:
            pid_out.append(pid.calc(i))
        print("pid calc: ",pid_out)
        plot_results(data,pid_out)

    # isolate out of control: pid = PID(27,.7,.5,1,1)
    def test_pid_driving(self):
        pid = PID(55,.5,0.05,0.05,1)
        pid_out = []
        steering_path=[]
        steering = 27
        for x in range(100):
            steering=steering+randrange(4)
            out = pid.calc(steering)
            pid_out.append(out)
            steering=clamp(out,-3,3)+steering
            steering_path.append(steering)

        # sim of changing light / color threshhold
        pid.updateTarget(0)
        for x in range(100):
            steering=steering+randrange(4)
            out = pid.calc(steering)
            pid_out.append(out)
            steering=clamp(out,-4,4)+steering
            steering_path.append(steering)

        plot_results(steering_path,pid_out)

if __name__ == "__main__":
    unittest.main()