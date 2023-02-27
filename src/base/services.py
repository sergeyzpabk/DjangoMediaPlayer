from django.core.exceptions import ValidationError


def get_path_upload_avatar(instanse,file):
    """ Построение пути в файлу format: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/{instanse.id}/file'

def validate_size_image(file_obj):
    """Проверка размера
    """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit* 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {megabyte_limit}MB")