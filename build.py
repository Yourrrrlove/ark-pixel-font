import logging

import configs
from configs import workspace_define
from services import design_service, font_service, info_service
from utils import fs_util

logging.basicConfig(level=logging.DEBUG)


def main():
    fs_util.cleanup_dir(workspace_define.outputs_dir)
    for font_config in configs.font_configs:
        design_service.classify_design_files(font_config)
        design_service.verify_and_handle_design_files(font_config)
        alphabet_map, design_file_paths_map = design_service.collect_available_design(font_config)
        font_service.make_fonts(font_config, alphabet_map, design_file_paths_map)
        info_service.make_info_file(font_config, alphabet_map)
        info_service.make_preview_image_file(font_config)
        info_service.make_alphabet_txt_file(font_config, alphabet_map)
        info_service.make_alphabet_html_file(font_config, alphabet_map)
        info_service.make_demo_html_file(font_config)


if __name__ == '__main__':
    main()
