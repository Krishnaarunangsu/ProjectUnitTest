import pytest
from pymongo import MongoClient

@pytest.fixture
def setup_users():
    mongo_db = connect()
    mongo_db["users"].delete_one({"uid": "user1"})
    mongo_db["users"].delete_one({"uid": "user2"})
    mongo_db["users"].delete_one({"uid": "admin1"})
    mongo_db["users"].delete_one({"uid": "superuser1"})
    mongo_db["users"].delete_one({"uid":"!@#$%^&*()[]\":;"})
    mongo_db["users"].delete_one({"uid":"naveensinha"})
    mongo_db["users"].delete_one({"uid":"harikp"})
    mongo_db["users"].insert_one({"uid": "user1",
        "pwd": "$6$rounds=656000$GIoMhgo5wP0aE9SZ$npCRGwWMVwlwIsLQzs5uRzz1iPKhYP/ow0Y2YEFNgSCATMqub8SMUP6JAdZtPIJYzSRugtTNEowDHXPu7o7nn.",
                              "firstName": "user1", "lastName": "user1", "email": "user1@abzooba.com", "primaryRole": "Dev",
                              "loginStatus": False, "activationStatus": True})
    # mongo_db["users"].insert_one({"uid": "user2",
        # "pwd": "$6$rounds=656000$ou7mZFl4hvgSrnWd$dWg4qndWazoBvFclmJQBCrLm0hZgpC36ArOsOXs8YmSS0ncuH0L2SzgY1Plmib3xpbgExynbgZp9KJoa4bAh9.",
        #                     "firstName": "user2", "lastName": "user2", "email": "user2@abzooba.com", "primaryRole": "Dev",
        #                     "loginStatus": False, "activationStatus": True})
    mongo_db["users"].insert_one({"uid": "admin1",
        "pwd": "$6$rounds=656000$6O2H0JI8GDlwdubY$Gnie7EpzLvWBmzxMHgxPy0QasgnqvkRFADE/1IcsuFR.qvgm2/VTwpLJ4wIP80FPRyOL1rKm9eny7gAVpKTev/",
                              "firstName": "admin1", "lastName": "admin1", "email": "admin1@abzooba.com", "primaryRole": "Admin",
                              "loginStatus": False, "activationStatus": True})
    mongo_db["users"].insert_one({"uid": "superuser1",
        "pwd": "$6$rounds=656000$u2H46.TctNJqnu.p$uo5PoQJML9LuyUUgEGgDoD0wptwzuc.0Yd4sRCkcoQb/x5hWMa6JCN4jh.yjqQLQJrCNWXqfINdNLKygC3b021",
                              "firstName": "superuser1", "lastName": "superuser1", "email": "superuser1@abzooba.com", "primaryRole": "Su",
                              "loginStatus": False, "activationStatus": True})


    return 1

@pytest.fixture
def setup_users_for_projects():
    setup_users()
    mongo_db = connect()
    mongo_db["users"].delete_one({"uid": "user3"})
    mongo_db["users"].insert_one({"uid": "user3",
        "pwd": "$6$rounds=656000$L6ypUvOo04Pffi5d$U50Of4a0rDGGzeiwPhjNl6k9kdH63RuPNHr/wb9U.PrF4ylX0.6IEKvkAMie7xoQCbe/jKUENEi3aRtukXoJd1",
                              "firstName": "user3", "lastName": "user3", "email": "user3@abzooba.com", "primaryRole": "Dev",
                              "loginStatus": False, "activationStatus": True})
    mongo_db["users"].insert_one({"uid": "user2",
        "pwd": "$6$rounds=656000$ou7mZFl4hvgSrnWd$dWg4qndWazoBvFclmJQBCrLm0hZgpC36ArOsOXs8YmSS0ncuH0L2SzgY1Plmib3xpbgExynbgZp9KJoa4bAh9.",
                             "firstName": "user2", "lastName": "user2", "email": "user2@abzooba.com", "primaryRole": "Dev",
                             "loginStatus": False, "activationStatus": True})


    return 1


@pytest.fixture
def setup_nodes():
    mongo_db = connect()
    mongo_db["nodes"].delete_one({"address": "172.16.1.171"})
    mongo_db["nodes"].delete_one({"address": "172.16.1.172"})
    mongo_db["nodes"].delete_one({"address": "172.16.1.173"})
    mongo_db["nodes"].delete_one({"address": "172.16.1.174"})
    return 1


@pytest.fixture
def setup_projects():
    mongo_db = connect()
    mongo_db["projects"].delete_one({"name": "project2"})
    return 1


@pytest.fixture
def setup_nodes_for_deactivation():
    mongo_db = connect()
    mongo_db["nodes"].delete_one({"address": "172.16.1.171"})
    mongo_db["nodes"].delete_one({"address": "172.16.1.172"})
    mongo_db["nodes"].delete_one({"address": "172.16.1.173"})
    mongo_db["nodes"].delete_one({"address": "172.16.1.174"})
    mongo_db["nodes"].insert_one({"address": "172.16.1.171", "nodetype": "DEV_VM", "user_or_cluster": "user1"})
    mongo_db["nodes"].insert_one({"address": "172.16.1.172", "nodetype": "CLUSTER_MASTER", "user_or_cluster": "cluster1"})
    mongo_db["nodes"].insert_one({"address": "172.16.1.173", "nodetype": "CLUSTER_WORKER", "user_or_cluster": "cluster1"})
    return 1


@pytest.fixture
def setup_clusters():
    mongo_db = connect()
    mongo_db["clusters"].delete_many({})
    mongo_db["clusters"].insert_one({"name": "cluster1", "activationStatus": True})


    return 1


def connect():
    mongo_db = None
    if mongo_db is None:
        mongo_client = MongoClient(host="mongodb://172.16.3.1:27017/?replicaSet=rs0", w=1)
        #mongo_client = MongoClient()
        mongo_db = mongo_client["xprdb"]
        #mongo_db = mongo_client["xpresso_ai"]
        mongo_db.authenticate("xprdb_admin", "xprdb@Abz00ba")
    return mongo_db
