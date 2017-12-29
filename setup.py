from distutils.core import setup, Extension

dallar_subsidy_module = Extension('dallar_subsidy', sources = ['dallar_subsidy.cpp'])

setup (name = 'dallar_subsidy',
       version = '1.0',
       description = 'Subsidy function for Dallar',
       ext_modules = [dallar_subsidy_module])
