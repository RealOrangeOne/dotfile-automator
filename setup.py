from setuptools import setup

setup (
	name='dotfile-automator',
	version='0.0',
	install_requires=[
		'click',
        'PyYaml'
	],
	entry_points='''
		[console_scripts]
		dfa=project.cli:cli
	''',
)
