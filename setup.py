from setuptools import setup

setup(
    name='password_manager',
    version='1.0',
    description='Password Manager CLI Tool',
    author='DavidH',
    author_email='davidhvcahun@hotmail.com',
    packages=['app'],
    install_requires=[
        # list
        # 'requests>=2.25.1',
    ],
    entry_points={
        'console_scripts': [
            'psswrd=app.main:main',
        ],
    },
)
