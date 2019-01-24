import os
import subprocess
import sys
import tempfile
import urllib
import urlparse

# download script
script_url = sys.argv[1]
script_filename = os.path.basename(urlparse.urlparse(script_url).path)
script_path = os.path.join(tempfile.gettempdir(), script_filename)
print 'Downloading %s to %s' % (script_url, script_path)
urllib.urlretrieve(script_url, script_path)

# run script
script_args = sys.argv[2:]
subprocess.call([sys.executable, script_path] + sys.argv[2:])
