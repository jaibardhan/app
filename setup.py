from setuptools import setup, find_packages
#pip install csvreader
setup(
    name='installerpy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    entry_points={
        'console_scripts': [
            # 'command=module:function'
        ],
    },
    author='Jai Bardhan',
    author_email='jaibardhan@example.com',
    description='A test module your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
