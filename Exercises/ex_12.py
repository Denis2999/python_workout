def get_file_extension(file_name):
    if "." in file_name:
        return file_name.split('.')[-1]
    raise Exception("Can not get a file extension")


print(get_file_extension("fasdfarsf.fru"))
