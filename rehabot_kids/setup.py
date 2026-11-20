
from setuptools import find_packages, setup

package_name = 'rehabot_kids'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rehabot_kids',
    maintainer_email='user@example.com',
    description='Robot asistencial para acompañamiento y estimulacion cognitiva',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cognitive_game = rehabot_kids.cognitive_game_node:main',
        ],
    },
)
