from modules.bin import *

source = [10,20]
def def1(index, source = None):
  if source is None:
    result = index * 2
  else:
    result = source[0] * 2
  fn_log(f"{index}: {result = }")

multithreading(
    call_def = def1,
    source = source,
    threads = 2,
)