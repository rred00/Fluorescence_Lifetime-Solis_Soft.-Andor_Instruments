#!/usr/bin/env python
# coding: utf-8



import numpy as np
import pandas as pd

class ASCIIDataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.info_dict = {}
        self.skip = 0
        self.acqui_mode = None
        self.gate_width = None
        self.gate_step = None
        self.acqui_time = None
        self.data = None
        self.cube = None

    def parse_header(self):
        """Read header info and detect skip rows."""
        with open(self.filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if ":" in line:
                    key, values = line.split(":", 1)
                    self.info_dict[key.strip()] = values.strip()
                if all(c.isdigit() or c in ".-+e," for c in line):
                    break
                self.skip += 1
        
        # Extract acquisition parameters
        self.acqui_mode = self.info_dict.get('Acquisition Mode')
        self.gate_width = int(self.info_dict.get('Gate Width (nsecs)'))
        self.gate_step = int(self.info_dict.get('Gate Delay Step (nsecs)'))
        self.acqui_time = int(self.info_dict.get('Number in Kinetics Series'))

    

    def build_cube(self):
        """Load numeric data into a DataFrame."""
        # First read to detect number of columns
        df = pd.read_csv(self.filepath, skiprows=self.skip, sep=',')
        y = len(df.iloc[1, 0:])
        col = np.arange(y)

        # Re-read with proper column names
        df = pd.read_csv(self.filepath, skiprows=self.skip, sep=',', names=col)
        self.data = df.copy()
        
        """Build 3D data cube [time, y, x]."""


        pix_y = self.data.iloc[:, 0].unique()
        ypix_total = len(pix_y)

        nanpix = [pixel for pixel in self.data.columns if self.data[pixel].isnull().sum() > 0]
        pix_x = self.data.iloc[0, 1:nanpix[0]]
        xpix_total = len(pix_x)

        print(f"Total pixels → X: {xpix_total}, Y: {ypix_total}")

        cube = np.zeros((self.acqui_time, ypix_total, xpix_total))

        for k in range(self.acqui_time):
            for i in range(ypix_total):
                for j in range(xpix_total):
                    cube[k, i, j] = self.data.iloc[ypix_total * k + i, j + 1]

        self.cube = cube
        return cube

    def summary(self):
        """Print acquisition summary."""
        print(f"Mode: {self.acqui_mode}, Gate Width: {self.gate_width} ns, Gate Step: {self.gate_step} ns")
        print(f"Number of scans: {self.acqui_time}")







