from data_access_layer.implementation_classes.manager_postgres_dao import ManagerPostgresDAO

manager_dao = ManagerPostgresDAO()


def test_select_all_manager_information_by_manager_id():
    manager = manager_dao.get_manager_information_by_id(4)
    assert manager.manager_id == 4
