
Munin Plugins for MongoDB
============

Plugins
----------
* mongo_ops   : operations/second
* mongo_mem   : mapped, virtual and resident memory usage
* mongo_btree : btree access/misses/etc...
* mongo_conn  : current connections
* mongo_lock  : write lock info
* mongo_docs  : number of documents (inserted, updated...)
* mongo_lag   : replication lag in seconds

Requirements
-----------
* MongoDB 2.4+
* python/pymongo

Installation (ubuntu)
------------

**Install pymongo:**

    sudo apt-get install pip
    sudo apt-get install build-essential python-dev
    sudo pip install pymongo
or

    sudo apt-get install python-pymongo

**Install plugins**

    git clone https://github.com/arep/mongo-munin.git /tmp/mongo-munin
    sudo cp /tmp/mongo-munin/mongo_* /usr/share/munin/plugins
    sudo ln -sf /usr/share/munin/plugins/mongo_btree /etc/munin/plugins/mongo_btree
    sudo ln -sf /usr/share/munin/plugins/mongo_conn /etc/munin/plugins/mongo_conn
    sudo ln -sf /usr/share/munin/plugins/mongo_lock /etc/munin/plugins/mongo_lock
    sudo ln -sf /usr/share/munin/plugins/mongo_mem /etc/munin/plugins/mongo_mem
    sudo ln -sf /usr/share/munin/plugins/mongo_ops /etc/munin/plugins/mongo_ops
    sudo ln -sf /usr/share/munin/plugins/mongo_docs /etc/munin/plugins/mongo_docs
    sudo ln -sf /usr/share/munin/plugins/mongo_lag /etc/munin/plugins/mongo_lag
    sudo chmod +x /usr/share/munin/plugins/mongo_*
    sudo service munin-node restart

Check if plugins are running:

    munin-node-configure | grep "mongo_"

Test plugin output:

    munin-run mongo_ops

Notes
-----------
* Authentication needs to be re-added
