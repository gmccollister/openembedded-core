from oeqa.oetest import oeSDKTest, skipModule
from oeqa.utils.decorators import *
from oeqa.utils.targetbuild import SDKBuildProject

def setUpModule():
    if not (oeSDKTest.hasPackage("gtk+3") or oeSDKTest.hasPackage("libgtk-3.0")):
        skipModule("Image doesn't have gtk+3 in manifest")

class GalculatorTest(oeSDKTest):
    def test_galculator(self):
        try:
            project = SDKBuildProject(oeSDKTest.tc.sdktestdir + "/galculator/",
                                      oeSDKTest.tc.sdkenv, oeSDKTest.tc.d,
                                      "http://galculator.mnim.org/downloads/galculator-2.1.4.tar.bz2")

            project.download_archive()

            self.assertEqual(project.run_configure(), 0,
                            msg="Running configure failed")

            self.assertEqual(project.run_make(), 0,
                            msg="Running make failed")
        finally:
            project.clean()
