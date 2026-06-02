# PyInstaller hook for torch
# torch.classes is a C++ extension namespace, not a Python module.
# PyInstaller cannot analyze it and triggers:
#   "Examining the path of torch.classes raised: Tried to instantiate class '__path__._path'..."
# Declare excludedimports at the torch level to prevent PyInstaller
# from attempting to analyze torch.classes during module graph construction.

excludedimports = ['torch.classes']
