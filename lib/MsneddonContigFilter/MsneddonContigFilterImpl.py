#BEGIN_HEADER
from biokbase.workspace.client import Workspace as workspaceService
#END_HEADER


class MsneddonContigFilter:
    '''
    Module Name:
    MsneddonContigFilter

    Module Description:
    A KBase module: MsneddonContigFilter
This sample module contains one small method - count_contigs.
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    #BEGIN_CLASS_HEADER
    workspaceURL = None
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        #END_CONSTRUCTOR
        pass

    def filter_contigs(self, ctx, workspace_name, contigset_id, min_length):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN filter_contigs
        #END filter_contigs

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method filter_contigs return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
