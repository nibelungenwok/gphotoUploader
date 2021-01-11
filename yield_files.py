import os
import pickle

def is_file_matched_ext(ext, filename_with_ext):
    filename_without_ext, file_ext = os.path.splitext(filename_with_ext)
    # file_ext contains a leading '.' so we need to do [1:]
    if file_ext[1:].lower() == ext.lower():
        return True
    return False

def yield_matched_files_to_be_upload(dir_path, target_ext):
    print('yield_matched_files_to_be_upload')
    iter_file_pathes = None
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        iter_file_pathes = os.scandir(dir_path)
        assert iter_file_pathes is not None
         
        for file_path in iter_file_pathes:
            if file_path.is_file() and is_file_matched_ext(target_ext, file_path.name):
                yield file_path
                
def yield_matched_files(dir_path, target_ext):
    print('yield_matched_files')
    iter_file_pathes = None
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        iter_file_pathes = os.scandir(dir_path)
        assert iter_file_pathes is not None
         
        for file_path in iter_file_pathes:
            if file_path.is_file() and is_file_matched_ext(target_ext, file_path.name):
                yield file_path


def yield_every_n_minus_one_path(iter_path_of_images, max_number_image):
    print('yield_every_n_minus_one_path') 
    batch_image_pathes = []
    for path in iter_path_of_images:
        # get 49 image paths 
        print(f'path: {path}')
        batch_image_pathes.append(path)
        if len(batch_image_pathes) == max_number_image - 1:
            print('batch full')
            yield batch_image_pathes 
            batch_image_pathes = []
        
    if batch_image_pathes:
        print('last batch')
        # cannot use return here
        yield batch_image_pathes 
