"""The bootstrap script for virtualenv."""

import os
import sys
import subprocess
import virtualenv


def after_install(_, home_dir):
  """Perform additional steps after installation."""
  pip_path = os.path.join(home_dir, 'bin', 'pip')
  subprocess.call([pip_path, 'install', '-U', 'pip'])
  subprocess.call([pip_path, 'install', '-r', 'requirements.txt'])
  subprocess.call([pip_path, 'install', '-e', '.'])


virtualenv.after_install = after_install


sys.argv = ['virtualenv', 'ENV']
virtualenv.main()