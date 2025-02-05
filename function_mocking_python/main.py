from typing import Optional


def enough_files(storage_path: str, threshold: int) -> bool:
  if get_number_of_files(storage_path) < threshold:
    return False
  return True


def get_number_of_files(storage_path: str) -> Optional[int]:
  """
  Return the number of files from storage
  """
  try:
    return len(dbutils.fs.ls(storage_path))
  except Exception as e:
    return None
