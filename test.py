import unittest

class PackageTest(unittest.TestCase):
  def test_pack_build(self):
    import subprocess
    subprocess.call('python setup.py sdist')

def suite():
  suite = unittest.TestLoader().loadTestsFromTestCase(PackageTest)
  return suite
  
def run():
  import mikroapp.test
  test_suite = unittest.TestSuite()
  tests=mikroapp.test.suite()
  print tests
  test_suite.addTest(tests)  
  packtests=suite()
  test_suite.addTest(packtests)
  unittest.TextTestRunner(verbosity = 2).run(test_suite)

if __name__ == '__main__':
  run()
  
  
