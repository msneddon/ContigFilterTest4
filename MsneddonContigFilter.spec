/*
A KBase module: MsneddonContigFilter
This sample module contains one small method - count_contigs.
*/

module MsneddonContigFilter {
	/*
	A string representing a ContigSet id.
	*/
	typedef string contigset_id;
	
	/*
	A string representing a workspace name.
	*/
	typedef string workspace_name;

	typedef structure {
		string new_contigset_ref;
		int n_initial_contigs;
		int n_contigs_removed;
		int n_contigs_remaining;
	} FilterContigsResults;
	
	/*
	Count contigs in a ContigSet
	contigset_id - the ContigSet to count.
	*/
	funcdef filter_contigs(workspace_name,contigset_id, int min_length) returns (FilterContigsResults) authentication required;
};