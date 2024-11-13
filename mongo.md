<!-- ref: https://www.mongodb.com/developer/products/mongodb/cheat-sheet/ -->

Show Databases
```sh
show dbs
db // prints the current database
```

Switch Database
```sh
use <database_name>
```

Show Collections.
```sh
show collections
```


Insert
```sh
# coll = name of the collection
# db.<collection name>.insertOne({name: "Max"})
db.coll.insertOne({name: "Max"})
```

Read
```sh
db.coll.findOne() // returns a single document
db.coll.find()    // returns a cursor - show 20 results - "it" to display more
db.coll.find().pretty()
db.coll.find({name: "Max", age: 32}) // implicit logical "AND".
db.coll.find({date: ISODate("2020-09-25T13:57:17.180Z")})
db.coll.find({name: "Max", age: 32}).explain("executionStats") // or "queryPlanner" or "allPlansExecution"
db.coll.distinct("name")


// Comparison
db.coll.find({"year": {$gt: 1970}})
db.coll.find({"year": {$gte: 1970}})
db.coll.find({"year": {$lt: 1970}})
db.coll.find({"year": {$lte: 1970}})
db.coll.find({"year": {$ne: 1970}})
db.coll.find({"year": {$in: [1958, 1959]}})
db.coll.find({"year": {$nin: [1958, 1959]}})
```


Python SKD mongo

```py
# To avoid ! in the title
kwargs["key"] = {"$not": {"$regex": "/!/"}}
```