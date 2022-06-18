from setuptools import setup, find_packages


setup(name='zedmath',
    version='1.0.0',
    description='Math operations',
    author='www.AZIZBEKDEV.com',
    author_email='azizbekqozoqovinfo@gmail.com',
    url='https://www.azizbekdev.com',
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Education',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3',
          ],
)