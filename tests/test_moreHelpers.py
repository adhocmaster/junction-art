import unittest
import extensions
import os
from library.Configuration import Configuration

class test_moreHelper(unittest.TestCase):

    def setUp(self):
        
        self.configuration = Configuration()
        self.esminiPath = self.configuration.get("esminipath")
        self.rootPath = self.configuration.get('rootPath')


    def test_saveRoadImageFromFile(self):

        xodrPath = self.rootPath + "\\output\\test-RightLane.xodr"
        outputFile = extensions.saveRoadImageFromFile(xodrPath, self.configuration.get("esminipath"))
        assert os.path.isfile(outputFile)

