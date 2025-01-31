-Access the terminal of DB :
kubectl exec -it mongodb-0 --namespace=aloussaief -- mongosh
-Replica_set initiation :
rs.initiate({_id: "rs0",members: [{ _id: 0, host: "mongodb-0.mongodb-service.aloussaief.svc.cluster.local:27017" },{ _id: 1, host: "mongodb-1.mongodb-service.aloussaief.svc.cluster.local:27017" },{ _id: 2, host: "mongodb-2.mongodb-service.aloussaief.svc.cluster.local:27017" }]})
rs.status()
-To allow the secondary DB(slave) to access the master DB :
db.getMongo().setReadPref("secondary")
- To test that it functions properly : 
Add data from primary : db.test_collection.insertOne({ "name": "Achref", "role": "Student" })
Retrieve it from the secondary : db.test_collection.find().pretty()