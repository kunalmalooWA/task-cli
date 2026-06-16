from setuptools import setup

setup(
    name = "my-task-tool",
    version="1.0",
    py_modules=["main"],
    entry_points={
        'console_scripts': [
            'task-cli=main:main'
        ]
    },
)