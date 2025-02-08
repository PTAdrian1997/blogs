from typing import Optional


def get_number_of_files(storage_path: str) -> Optional[int]:
  """
  Return the number of files from storage
  """
  try:
    return len(dbutils.fs.ls(storage_path))
    # return 3
  except Exception as e:
    return None
