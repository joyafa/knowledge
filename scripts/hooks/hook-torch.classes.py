# PyInstaller hook for torch.classes
# torch.classes is a C++ extension namespace, not a Python module.
# PyInstaller cannot analyze it and triggers a harmless warning:
#   "Examining the path of torch.classes raised: Tried to instantiate class '__path__._path'..."
# This hook tells PyInstaller to skip analyzing this namespace entirely.

excludedimports = ['torch.classes']
