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

        token = ctx['token']
        ws = workspaceService(self.workspaceURL, token=token)
        contigSet = ws.get_objects([{'ref': workspace_name+'/'+contigset_id}])[0]['data']
        provenance = None
        if 'provenance' in ctx:
            provenance = ctx['provenance']
            # add additional info to provenance here if needed

        # save the contigs to a new list
        good_contigs = []
        n_total = 0;
        n_remaining = 0;
        for contig in contigSet['contigs']:
            n_total += 1
            if len(contig['sequence']) >= min_length:
                good_contigs.append(contig)
                n_remaining += 1

        # replace the contigs in the contigSet object in local memory
        contigSet['contigs'] = good_contigs

        # save the new object to the workspace
        obj_info_list = ws.save_objects({
                            'workspace':workspace_name,
                            'objects': [
                                {
                                    'type':'KBaseGenomes.ContigSet',
                                    'data':contigSet,
                                    'name':contigset_id,
                                    'provenance':provenance
                                }
                            ]
                        })
        info = obj_info_list[0]


        returnVal = {
                'new_contigset_ref': str(info[6]) + '/'+str(info[0])+'/'+str(info[4]),
                'n_initial_contigs':n_total,
                'n_contigs_removed':n_total-n_remaining,
                'n_contigs_remaining':n_remaining
            }
        #END filter_contigs

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method filter_contigs return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
