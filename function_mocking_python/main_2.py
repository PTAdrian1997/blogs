from function_mocking_python.main import get_number_of_files


def enough_files(storage_path: str, threshold: int) -> bool:
  if get_number_of_files(storage_path) < threshold:
    return False
  return True