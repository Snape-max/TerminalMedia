from setuptools import setup, find_packages

setup(
    name='imgcat',
    version='0.1.0',
    description='A tool to display images in the terminal',
    author='Snape-max',
    author_email='ssnape@qq.com',
    url='https://github.com/Snape-max/imgcat',  # 你的项目主页
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'imgcat=imgcat.imgcat:main',
        ],
    },
    install_requires=[
        'Pillow',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # 选择合适的许可证
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)