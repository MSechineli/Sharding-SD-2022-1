```
rs.initiate(
  {
    _id: "cfgrs",
    configsvr: true,
    members: [
      { _id : 0, host : "192.168.18.8:40001" },
      { _id : 1, host : "192.168.18.8:40002" },
      { _id : 2, host : "192.168.18.8:40003" }
    ]
  }
)
```

```
rs.initiate(
  {
    _id: "shard1rs",
    members: [
      { _id : 0, host : "192.168.18.8:50001" },
      { _id : 1, host : "192.168.18.8:50002" },
      { _id : 2, host : "192.168.18.8:50003" }
    ]
  }
)
```

```
rs.initiate(
  {
    _id: "shard2rs",
    members: [
      { _id : 0, host : "192.168.18.8:50004" },
      { _id : 1, host : "192.168.18.8:50005" },
      { _id : 2, host : "192.168.18.8:50006" }
    ]
  }
)
```

```bash
version: '3'

services:

  mongos:
    container_name: mongoserver
    image: mongo
    command: mongos --configdb cfgrs/192.168.18.8:40001,192.168.18.8:40002,192.168.18.8:40003 --bind_ip 0.0.0.0 --port 27017
    ports:
      - 60000:27017
```

```bash
sh.addShard("shard1rs/192.168.18.8:50001,192.168.18.8:50002,192.168.18.8:50003")
```

```bash
sh.addShard("shard2rs/192.168.18.8:50004,192.168.18.8:50005,192.168.18.8:50006")
```

