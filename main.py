from pyan.visgraph import VisualGraph
from pyan.analyzer import CallGraphVisitor
from pprint import pprint
import logging
from glob import glob
import os


def main():
    repo_paths = ['ecosystem\\**\\*.py']
    filenames = [fn for repo_path in repo_paths for fn in glob(repo_path, recursive=True)]
    filenames = list(filter(lambda filename: (os.path.sep + 'tests' + os.path.sep) not in filename and (os.path.sep + 'testing' + os.path.sep) not in filename, filenames))
    v = CallGraphVisitor(filenames)
    graph = VisualGraph.dump_callgraph(v)


if __name__ == '__main__':
    main()
