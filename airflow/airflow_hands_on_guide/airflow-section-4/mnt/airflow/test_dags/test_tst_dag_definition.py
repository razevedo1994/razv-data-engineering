import pytest
import collections
import pendulum
from airflow.models import DagBag

@pytest.fixture(scope="class")
def dag(dagbag):
    return dagbag.get_dag('tst_dag')

class TestTstDagDefinition:

    EXPECTED_NB_TASKS = 6
    EXPECTED_TASKS = ['task_1', 'task_2', 'task_3', 'task_4', 'task_5', 'task_6']

    compare = lambda self, x, y: collections.Counter(x) == collections.Counter(y)

    def test_nb_tasks(self, dag):
        """
            Verify the number of tasks in the DAG
        """
        nb_tasks = len(dag.tasks)
        assert nb_tasks == self.EXPECTED_NB_TASKS, "Wrong number of tasks, {0} expected, got {1}".format(self.EXPECTED_NB_TASKS, nb_tasks)

    def test_contain_tasks(self, dag):
        """
            Verify if the DAG is composed of the expected tasks
        """
        task_ids = list(map(lambda task: task.task_id, dag.tasks))
        assert self.compare(task_ids, self.EXPECTED_TASKS)

    @pytest.mark.parametrize("task, expected_upstream, expected_downstream", 
        [
            ("task_1", [], ["task_2"]), 
            ("task_2", ["task_1"], ["task_3", "task_4", "task_5"]), 
            ("task_3", ["task_2"], ["task_6"])
        ]
    )
    def test_dependencies_of_tasks(self, dag, task, expected_upstream, expected_downstream):
        """
            Verify if a given task has the expected upstream and downstream dependencies
            - Parametrized test function so that each task given in the array is tested with the associated parameters 
        """
        task = dag.get_task(task)
        assert self.compare(task.upstream_task_ids, expected_upstream), "The task {0} doesn't have the expected upstream dependencies".format(task)
        assert self.compare(task.downstream_task_ids, expected_downstream), "The task {0} doesn't have the expected downstream dependencies".format(task)

    def test_start_date_and_catchup(self, dag):
        """
            Verify that the start_date is < current date and catchup = False
        """
        True

    def test_same_start_date_all_tasks(self, dag):
        """
            Best Practice: All of your tasks should have the same start_date
        """
        tasks = dag.tasks
        start_dates = list(map(lambda task: task.start_date, tasks))
        assert len(set(start_dates)) == 1