from X.Database import db

pmdb = db.pm
pmwarn = db.pmwarn
pmap = db.pmapprove
warner = db.warner

async def toggle_pm():
    x = await pmdb.find_one({"pm": 0})
    if x:
        return await pmdb.delete_one({"pm": 0})
    else:
        return await pmdb.insert_one({"pm": 0})

async def is_pm_on():
    x = await pmdb.find_one({"pm": 0})
    if x:
        return True
    return False

async def update_warns(w: int):
    await pmwarn.update_one({"w": "w"}, {"$set": {"warns": w}}, upsert=True)

async def limit():
    x = await pmwarn.find_one({"w": "w"})
    if not x:
        return 0
    return x["warns"]

async def approve(user_id: int):
    x = await pmap.find_one({"user_id": user_id})
    if x:
        return
    await pmap.insert_one({"user_id": user_id})

async def disapprove(user_id: int):
    x = await pmap.find_one({"user_id": user_id})
    if not x:
        return
    await pmap.delete_one({"user_id": user_id})

async def is_approved(user_id: int):
    x = await pmap.find_one({"user_id": user_id})
    if x:
        return True
    return False

async def list_approved():
    x = pmap.find({"user_id": {"$gt": 0}})
    if not x:
        return []
    g = []
    for h in await x.to_list(length=1000000000):
        g.append(h["user_id"])
    return g

async def add_warn(user_id: int):
    x = await warner.find_one({"user_id": user_id})
    if x:
        l = x["warns"]
        l += 1
        return await warner.update_one({"user_id": user_id}, {"$set": {"warns": l}}, upsert=True)
    return await warner.update_one({"user_id": user_id}, {"$set": {"warns": 1}}, upsert=True)

async def reset_warns(user_id: int):
    return await warner.update_one({"user_id": user_id}, {"$set": {"warns": 0}}, upsert=True)

async def get_warns(user_id: int):
    x = await warner.find_one({"user_id": user_id})
    if x:
        l = x["warns"]
        return l
    return 0
