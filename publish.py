import logging

import configs
from configs import workspace_define
from services import publish_service
from utils import fs_util

logging.basicConfig(level=logging.DEBUG)


def main():
    fs_util.cleanup_dir(workspace_define.releases_dir)
    for font_config in configs.font_configs:
        publish_service.make_release_zips(font_config)
        publish_service.copy_font_related_files(font_config)
    publish_service.copy_other_files()


if __name__ == '__main__':
    main()
