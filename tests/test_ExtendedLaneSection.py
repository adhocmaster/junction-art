import pyodrx
import junctions


import unittest

import numpy as np
import os, dill
import pyodrx 
from junctions.JunctionMerger import JunctionMerger
import extensions
from library.Configuration import Configuration
from junctions.JunctionBuilder import JunctionBuilder
from junctions.RoadBuilder import RoadBuilder
from junctions.LaneBuilder import LaneBuilder

from junctions.LaneLinker import LaneLinker

from extensions.LaneOffset import LaneOffset


class test_LaneBuilder(unittest.TestCase):

    def setUp(self):
        self.configuration = Configuration()
        self.laneBuilder = LaneBuilder()

    
    def test_widths(self):

        roadLength = 10

        #1 simple Lanes

        lanes = self.laneBuilder.getStandardLanes(1, 3)

        for laneSec in lanes.lanesections:
            widths = laneSec.widths(roadLength)
            assert widths[0] == 6
            assert widths[1] == 6

        
        #1 turn lanes

        lanes = self.laneBuilder.getStandardLanes(1, 3, roadLength=roadLength, isLeftTurnLane=True, isRightTurnLane=True)


        widths = lanes.lanesections[0].widths(roadLength, LaneOffset(s=0), LaneOffset(s=1))
        print(widths)
        assert widths[0] == 6
        assert widths[1] == 6

        widths = lanes.lanesections[1].widths(roadLength, LaneOffset(s=1), LaneOffset(s= roadLength - 1))
        print(widths)
        assert widths[0] == 6
        assert widths[1] == 12

        widths = lanes.lanesections[2].widths(roadLength, LaneOffset(s= roadLength - 1))
        print(widths)
        assert widths[0] == 12
        assert widths[1] == 12

        #2 merge lanes

        lanes = self.laneBuilder.getStandardLanes(1, 3, roadLength=roadLength, isLeftMergeLane=True, isRightMergeLane=True)


        widths = lanes.lanesections[0].widths(roadLength, LaneOffset(s=0), LaneOffset(s=1))
        print(widths)
        assert widths[0] == 12
        assert widths[1] == 12

        widths = lanes.lanesections[1].widths(roadLength, LaneOffset(s=1), LaneOffset(s= roadLength - 1))
        print(widths)
        assert widths[0] == 12
        assert widths[1] == 6

        widths = lanes.lanesections[2].widths(roadLength, LaneOffset(s= roadLength - 1))
        print(widths)
        assert widths[0] == 6
        assert widths[1] == 6
        
        #2 internal lanes

        lanes = self.laneBuilder.getStandardLanesWithInternalTurns(1, 3, roadLength=roadLength, numberOfLeftTurnLanesOnRight=2)


        widths = lanes.lanesections[0].widths(roadLength, LaneOffset(s=0), LaneOffset(s=1))
        print(widths)
        assert widths[0] == 12
        assert widths[1] == 12

        widths = lanes.lanesections[1].widths(roadLength, LaneOffset(s=1), LaneOffset(s= roadLength - 1))
        print(widths)
        assert widths[0] == 12
        assert widths[1] == 12

        widths = lanes.lanesections[2].widths(roadLength, LaneOffset(s= roadLength - 1))
        print(widths)
        assert widths[0] == 12
        assert widths[1] == 12


            
