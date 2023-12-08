from setuptools import setup, find_namespace_packages

setup(
    name='sort_folder2323',
    version='0.0.1',
    description='my first project',
    author='Taras',
    author_email='tarasakimec9@gmail.com',
    url='https://github.com/aps06/clean_folders/blob/2aacea58f7bc351a9f1dfb910a53f43612b7687e/sort_folder.py',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages=find_namespace_packages(),

    entry_points={'console_scripts':[f'clean_folders=clean_folder.sort_folder:run']}
)