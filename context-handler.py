#!/usr/bin/env python3

# import sys
from ast import arg
import os
import argparse

def context_parser(project_path, ignore_path):
    if ignore_path == '0':
        ignore = ['.venv', 'venv', '.git', 'gitignore', 'requirements.txt', 'context.txt', 'ignore']
    else:
        ignore = []
        with open(ignore_path) as file:
            for _ in file:
                ignore.append(_.strip())

    if project_path in ['./', '.', '.\\', ' ',]:
        path = os.getcwd()
    else:
        path = project_path
    k = 0
    with open('./context.txt', 'w') as context:
        for root, dirs, files in os.walk(path):
            print(root,'----', dirs,'----', files)
            k+=1
            for file in files:
                if any(_ in ' '.join((root,file)) for _ in ignore):
                    continue
                text_file = ''
                file_path = os.path.join(root, file) 
                with open(file_path) as src:
                    context.write(f'"{file_path}"\n')
                    text_file = src.readlines()
                    context.writelines(text_file)
                    context.writelines(['\n', '---\n', ])

def main():
    parser = argparse.ArgumentParser(description='cli context to text handler')

    #here we add arguments
    parser.add_argument(
        "--root",
        type=str,
        nargs='?',
        default='./',
        help='''Path to the root directory for context parsing (your project root).
                \n Current working directory ( ./ ) by default.'''
    )
    parser.add_argument(
        "--ignore",
        type=str,
        nargs='?',
        default='0',
        help='''Path to the file with dirs and files for the parser to ignore. \n
                It ignores .venv, venv, env, .git, gitignore and requirements.txt by default.'''
    )

    args = parser.parse_args()
    context_parser(args.root, args.ignore)
    

    

if __name__ == '__main__':
    main()

