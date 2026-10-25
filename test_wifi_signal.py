import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest
from wifi_signal import parse_proc_wireless
SAMPLE = "Inter-| sta-|   Quality        |   Discarded packets               | Missed | WE\n face | tus | link level noise |  nwid  crypt   frag  retry   misc | beacon | 22\n wlan0: 0000   62.  -48.  -256        0      0      0      0      0        0\n"
class T(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse_proc_wireless(SAMPLE), {"wlan0": -48})
    def test_empty(self):
        self.assertEqual(parse_proc_wireless("nothing here\n"), {})
if __name__ == "__main__": unittest.main()
