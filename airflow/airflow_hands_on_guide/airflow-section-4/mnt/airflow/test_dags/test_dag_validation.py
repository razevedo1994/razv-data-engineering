import pytest
from airflow.models import DagBag

class TestDagValidation:

    LOAD_SECOND_THRESHOLD = 2
    REQUIRED_EMAIL = "owner@test.com"
    EXPECTED_NUMBER_OF_DAGS = 7

    def test_import_dags(self, dagbag):
        """
            Verify that Airflow is able to import all DAGs
            in the repo
            - check for typos
            - check for cycles
        """
        assert len(dagbag.import_errors) == 0, "DAG failures detected! Got: {}".format(
            dagbag.import_errors
        )

    def test_time_import_dags(self, dagbag):
        """
            Verify that DAGs load fast enough
            - check for loading time
        """
        stats = dagbag.dagbag_stats
        slow_dags = list(filter(lambda f: f.duration > self.LOAD_SECOND_THRESHOLD, stats))
        res = ', '.join(map(lambda f: f.file[1:], slow_dags))        

        assert len(slow_dags) == 0, "The following DAGs take more than {0}s to load: {1}".format(
            self.LOAD_SECOND_THRESHOLD,
            res
        )

    @pytest.mark.skip(reason="not yet added to the DAGs")
    def test_default_args_email(self, dagbag):
        """
            Verify that DAGs have the required email
            - Check email
        """
        for dag_id, dag in dagbag.dags.items():
            emails = dag.default_args.get('email', [])
            assert self.REQUIRED_EMAIL in emails, "The mail {0} for sending alerts is missing from the DAG {1}".format(self.REQUIRED_EMAIL, dag_id)
    
    @pytest.mark.skip(reason="not yet added to the DAGs")
    def test_default_args_retries(self, dagbag):
        """
            Verify that DAGs have the required number of retries
            - Check retries
        """
        for dag_id, dag in dagbag.dags.items():
            retries = dag.default_args.get('retries', None)
            assert retries is not None, "You must specify a number of retries in the DAG: {0}".format(dag_id)

    @pytest.mark.skip(reason="not yet added to the DAGs")
    def test_default_args_retry_delay(self, dagbag):
        """
            Verify that DAGs have the required retry_delay expressed in seconds
            - Check retry_delay
        """
        for dag_id, dag in dagbag.dags.items():
            retry_delay = dag.default_args.get('retry_delay', None)
            assert retry_delay is not None, "You must specify a retry delay (seconds) in the DAG: {0}".format(dag_id)
 
    def test_number_of_dags(self, dagbag):
        """
            Verify if there is the right number of DAGs in the dag folder
            - Check number of dags
        """
        stats = dagbag.dagbag_stats
        dag_num = sum([o.dag_num for o in stats])
        assert dag_num == self.EXPECTED_NUMBER_OF_DAGS, "Wrong number of dags, {0} expected got {1} (Can be due to cycles!)".format(self.EXPECTED_NUMBER_OF_DAGS, dag_num)