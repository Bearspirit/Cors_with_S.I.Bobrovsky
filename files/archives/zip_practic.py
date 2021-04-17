from zipfile import ZipFile

with ZipFile("test_zip.zip", "a") as testzip:
    testzip.write('in_arch.txt')