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

    def __init__(self, databases_to_load = []):

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
        databases = self._load_databases()


    def load_raw(self):

        """

        Load the raw databases as requested per the user and return in a dataframe

        """

        pass

    def load_clean(self):

        """

        Load the cleaned versions of the databases

        """

        pass

    def load_subset(self, amount_of_rows_in_subset = 100, clean = True):

        """

        Load a subset of the dataframe.

        Arguments:
            amount_of_rows_in_subset (Int): How many rows of the data the user would like in their subset.
                                            Default: 100
                                            Note: We will maintain a subset of 100 for faster loading.
            clean (Bool): Load the clean version of the database, if not raw (this will take significantly longer)
                          Default: True
        """

        pass

    def load_training(self, return_complement = True):

        """

        Arguments:
            return_complement (Bool): If return the complement then return two values of 33% Training, 66% Dataset
        Returns:
            training_dataframe (Pandas DataFrame): dataframe of the 33% for training data
            training_complement_dataframe (Pandas DataFrame): dataframe of the 66% for the training data.


        """

        pass

    def _load_databases(self):

        """

        Private function to load the database

        Returns:
            databases (Pandas DF): the databases loaded into a dataframe


        UNIVERSE_CHEMICAL_DATAFRAME = {

            column_headers: *"smiles"*, "molecular_weight", "logp", "h_bond_donor", "h_bond_acceptor", "rotatable_bonds",
                            "number_of_atoms", "molar_refractivity", "topological_surface_area_mapping", "formal_charge",
                            "heavy_atoms", "num_of_rings"


        """

        # imports
        # -------
        import os
        from pathlib import Path


        # get the root directory
        root_directory = str(Path(__file__).parent.parent) + '/databases'

# Testing purposes
if __name__ == '__main__':

    LoadDatabases(databases_to_load=["binding"])