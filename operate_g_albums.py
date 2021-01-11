import logging
from setup_logger import setup_logger
from init_photo_service import build_service


ALBUM_ID_STORES_POWER_PLANT_SCREENSHOTS = 'ADBHGnakbEUBXLJSNg5sNVMPmmvLaVyewd_6FHC199nc6b4Sj2EJkT7m2HvGejUVXLlSj7bNqu9D'

logger = setup_logger(f'{__file__}',logging.DEBUG,f'{__file__}.log','a')
logger.debug('\n'+'*'*10+'Done setup logger')

# ToDo: capture build_service() failure
service = build_service()
logger.debug(f'Done setup service')

'''
create album
    you can create mulitple albums with same title, only their IDs are diff
    how to avoid creating a new album if an album with same names already exists
'''
def create_album(album_title):
    logger.debug('creating album begins')
    assert album_title is not None and album_title != ''
    '''
    inform user if there is a album with same title exists on the google photo
    user can have 2 options:
    still create 2 albums with same name(discouraging, cause user only remember 
    album title)
    choose a diff title to create new album 
    '''

    '''
    if there is no album with same title 
    we go ahead and create it
    '''
    request_body={
            'album':   {'title': album_title}
    }

    response_create_album = service.albums().create(body=request_body).execute()
    logger.debug(f'creating album, response:{response_create_album}')
    logger.debug('creating album done')
    return response_create_album 

# check if album created sucessfully

"""
list method, let user choose the list only the albums that are created by google api
or list all albums
"""
def find_album_by_title(title,is_only_app_created=True):
    #this assume the album is not empty
    lst_albums = return_all_albums(is_only_app_created)
    if lst_albums is not None:
        # search title in lst_albums
        for album in lst_albums:
            if title == album['title']:
                logger.debug(f'found album with title: {album["title"]}')
                # this will return the first album with matched title
                return album
        logger.bebug(f'No album matches given title')
        return None
    else:
        # no albums at all
        logger.debug(f'server has no album at all')
        return None


def return_all_albums(is_only_app_created=False, page_size=50):
    logger.debug('return albums')
    response = service.albums().list(
        pageSize=page_size,
        excludeNonAppCreatedData=is_only_app_created,
    ).execute()

    logger.debug('Done setup response')

    #lst_albums is a list
    #test if lst_albums is None(no albums qualified our query)
    
    lst_albums = response.get('albums')
    #logger.debug('*'*50 +f'lst_albums : {lst_albums}')
    nextPageToken = response.get('nextPageToken')
    while nextPageToken:
        response = service.albums.list(
            pageSize=page_size,
            excludeNonAppCreatedData=is_only_app_created,
            pageToken=nextPageToken
        )
        lst_albums.append(response.get('albums'))
        nextPageToken = response.get('nextPageToken')
        #ToDo is it possible to use yield here, in case there are too many albums
    return lst_albums

# albums should be returned by return_albums()
def yield_returned_albums(albums):
    if albums is not None:
        for album in albums:
            yield album
    else:
        logger.debug('in yield_return_albums, No albums given')

def list_albums(is_only_app_created=False, page_size=50):
    lst_albums = return_all_albums(is_only_app_created, page_size)
    logger.debug('Album List\n')
    if lst_albums is not None:
        for album in lst_albums:
            logger.debug(f'Album {album["title"]}:\n')
            #logger.debug(f'content of album obj: {album}')
            for key, value in album.items():
                logger.debug(f'{key}: {value}\n')
    else:
        # lst_albums is None
        logger.debug(f'No matched albums \n')
        # need to inform user 

'''
df_albums = pd.DataFrame(lst_albums)

print(f'df_albums:\n {df_albums}')
print(f'type of lst_albums:\n {type(lst_albums)}')
assert type(lst_albums) == type(list())

print(f'lst_albums[1]:\n {lst_albums[1]}')
print(f'lst_albums[0]:\n {lst_albums[0]}')
#exit()

'''
"""
search method (get all images inside an album by album id)
"""
#ToDo: the max number of photos in one album is 20k, so we need to create new ones
#album_id_created_by_our_app = 'ADBHGnYLBQ-UkBqK8ajvM-IJAOQwZK_Q6EVs0dkoTUpXkb8GwPYVbY0I41UYj-SKekRaFedr015b'

'''
this assume the album is not empty
media_files = service.mediaItems().search(body={'albumId': travel_album_id}).execute()['mediaItems']
'''
"""
request_body = {
        'albumId': album_id_created_by_our_app,
        'pageSize': 25
}
cloud_media_items = []
cloud_media_files_names = []
response = service.mediaItems().search(body=request_body).execute()
print(response)
if response:
    cloud_media_items = response['mediaItems']
    #print(f"media_files: {response['mediaItems']}")
    nextPageToken = response.get('nextPageToken')
    print(f'nextPageToken: {nextPageToken}') 
    #response = service.mediaItems().search(body={'albumId': album_id_created_by_our_app }).execute()

    while nextPageToken:
        request_body['pageToken'] = nextPageToken
        # don't use response = service.mediaItems().list( pageSize=25, pageToken=nextPageToken).execute()
        response = service.mediaItems().search(body=request_body).execute()

        cloud_media_items.extend(response['mediaItems']) 
        nextPageToken = response.get('nextPageToken')
        #print(f'in album:{album_id_created_by_our_app }')
        for media_file in cloud_media_items :
            print(f"image:{media_file['filename']}")
            cloud_media_files_names.append(media_file['filename']) 
else:
    print(f'no images in album:{album_id_created_by_our_app }')
# why cloud_media_files_names > set(cloud_media_files_names
# the correct number of photos is len(cloud_media_items)
print(len(cloud_media_files_names))
print(len(set(cloud_media_files_names)))
print(len(cloud_media_items))
"""


if __name__ == "__main__":
    title = 'taipower_109_06'
    #list_albums(False)
    list_albums(is_only_app_created=True)


    if find_album_by_title(title) is None:
        response = create_album('taipower_109_06')
        print(f'response create album: {response}')

    list_albums(is_only_app_created=True)
    album_found = find_album_by_title(title) 
    assert album_found is not None
    assert album_found['title'] == title 

