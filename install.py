#!/usr/bin/env python3

import os

os.environ['SYSTEM_VERSION_COMPAT'] = '0'

from facefusion import installer


def replace_name() -> None:
        custom_name = os.getenv('FACEFUSION_NAME') or input('Enter a custom name for FaceFusion (leave blank to keep default): ').strip()
        if custom_name:
                metadata_path = os.path.join(os.path.dirname(__file__), 'facefusion', 'metadata.py')
                with open(metadata_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                content = content.replace("'FaceFusion'", repr(custom_name))
                with open(metadata_path, 'w', encoding='utf-8') as file:
                        file.write(content)


if __name__ == '__main__':
        replace_name()
        installer.cli()
