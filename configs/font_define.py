import time

display_name = 'Ark Pixel'
unique_name = 'Ark-Pixel'
output_name = 'ark-pixel'
style_name = 'Regular'
version_name = '0.0.0-dev'
version_time = time.strftime("%Y%m%d")
version = f'{version_name}-{version_time}'
copyright_string = "Copyright (c) 2021, TakWolf (https://ark-pixel-font.takwolf.com), with Reserved Font Name 'Ark Pixel'."
designer = 'TakWolf'
description = 'Ark pixel font.'
vendor_url = 'https://ark-pixel-font.takwolf.com'
designer_url = 'https://takwolf.com'
license_description = 'This Font Software is licensed under the SIL Open Font License, Version 1.1.'
license_info_url = 'https://scripts.sil.org/OFL'


class FontConfig:
    def __init__(self, px, origin_y_px, em_dot_size=100):
        # 字体信息
        self.display_name = f'{display_name} {px}px'
        self.unique_name = f'{unique_name}-{px}px'
        # 字体参数
        self.px = px
        self.origin_y_px = origin_y_px
        self.em_dot_size = em_dot_size
        # 附加文件清单
        self.info_file_name = f'font-info-{px}px.md'
        self.preview_image_file_name = f'preview-{px}px.png'
        self.alphabet_txt_file_name = f'alphabet-{px}px.txt'
        self.alphabet_html_file_name = f'alphabet-{px}px.html'
        self.demo_html_file_name = f'demo-{px}px.html'

    def get_metrics(self):
        units_per_em = self.px * self.em_dot_size
        ascent = self.origin_y_px * self.em_dot_size
        descent = (self.origin_y_px - self.px) * self.em_dot_size
        return units_per_em, ascent, descent

    def get_output_display_name(self, language_specific):
        return f'{self.display_name} {language_specific}'

    def get_output_unique_name(self, language_specific):
        return f'{self.unique_name}-{language_specific}'

    def get_output_font_file_name(self, language_specific, font_format):
        return f'{output_name}-{self.px}px-{language_specific}.{font_format}'

    def get_release_zip_file_name(self, font_format):
        return f'{output_name}-font-{self.px}px-{font_format}-v{version}.zip'
