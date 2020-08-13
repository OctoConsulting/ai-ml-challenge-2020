from google_drive_downloader import GoogleDriveDownloader as gdd


def download_model_fr_drive():
    file_id = '1r-B3D-KvPrQqORoAF6cNyESBDhCofqxL'
    gdd.download_file_from_google_drive(file_id=file_id,
                                        dest_path='./model/model1.pt',)