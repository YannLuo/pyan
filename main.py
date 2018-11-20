from pyan.visgraph import VisualGraph
from pyan.analyzer import CallGraphVisitor
from pprint import pprint
import logging
from glob import glob
import os


def main():
    repo_path = ['REPOS\\pydantic\\pydantic\\**\\*.py']
    filenames = [fn2 for fn in repo_path for fn2 in glob(fn, recursive=True)]
    filenames = list(filter(lambda filename: (os.path.sep + 'tests' + os.path.sep) not in filename and (os.path.sep + 'testing' + os.path.sep) not in filename, filenames))
    logger = logging.getLogger(__name__)
    v = CallGraphVisitor(filenames, logger)
    graph = VisualGraph.dump_callgraph(v)
    print(graph)

if __name__ == '__main__':
    main()
