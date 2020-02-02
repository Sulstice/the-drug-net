#!/usr/bin/env python3
#
# Load the databases
#
# ------------------

# imports rdkit
# -------------
from rdkit import Chem

# Suppress RDKit's StdOut and StdErr
from rdkit import RDLogger
lg = RDLogger.logger()
lg.setLevel(RDLogger.CRITICAL)

# imports
# -------
import pandas as pd

class LoadDatabases(object):

    """


    Load the databases into dataframes

    Databases References:

        binding database:   A public, web-accessible database of measured binding affinities, focusing chiefly
                            on the interactions of protein considered to be drug-targets with small, drug-like
                            molecules.

                            https://www.bindingdb.org/bind/index.jsp

        withdrawn database: The database serves as a useful resource with information about the therapeutic (or primary)
                            targets, off-targets, toxicity types and biological pathways associated with the drugs in
                            the database.


    """

    __version__ = '0.0.1'

    # This is how we are going to track what databases we allow

    DATABASES = {
        "binding": "sdf",
        "withdrawn": "sdf",
    }

    def __init__(self, databases_to_load = [], load_raw = False, load_subset = False, load_training_set = False):

        """

        Initialize the loading of databases object

        Arguments:
            databases_to_load (List): the databasesm to load
            return_data_type (String): Option for the object to return to the user
            load_raw (Bool): Option whether to not merge any columns or have thedrugnet decide on merging of columns.

        Returns:
            database_data (Varied): Depends on the return data type for the user

        Databases Allowed:

            Withdrawn Database: Drugs that were withdrawn from the market: http://cheminfo.charite.de/withdrawn/index.html

        """

        self.databases_to_load = databases_to_load
        self.load_raw = load_raw

        databases = self._load_databases()


    def _detect_pickle_cache(self):

        """

        Detect the pickle cache version of a database
        :return:
        """


    def _load_databases(self):

        """

        Private function to load the database

        Returns:
            databases (Pandas DF): the databases loaded into a dataframe

        """

        # imports
        # -------
        import os

        # get the root directory
        root_directory = os.path.dirname(os.path.abspath(__file__)) + "/raw_resources"


        sorted_databases = sorted(self.databases_to_load)
        file_name = '_'.join(sorted_databases) + ".sdf"

        # First we need to detect if this has a pickle cache file
        for sub_directories, directories, files in os.walk(root_directory):
            for file in files:
                if file == file_name:
                    pass


# Testing purposes
if __name__ == '__main__':

    import pandas as pd

    binding_dataframe = pd.read_csv('/Users/sulimansharif/projects/the-drug-net/thedrugnet/raw_resources/BindingDB_All.tsv',sep='\t', error_bad_lines=False)

    print (binding_dataframe)