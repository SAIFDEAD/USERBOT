pm_data = {"pm": 0}
pmwarn_data = {"w": "w", "warns": 5}
pmap_data = []
warner_data = {}

async def toggle_pm():
    global pm_data
    if pm_data:
        pm_data = {}
    else:
        pm_data = {"pm": 0}

async def is_pm_on():
    global pm_data
    return bool(pm_data)

async def update_warns(w: int):
    global pmwarn_data
    pmwarn_data["warns"] = w

async def limit():
    global pmwarn_data
    return pmwarn_data.get("warns", 0)

async def approve(user_id: int):
    global pmap_data
    if user_id not in pmap_data:
        pmap_data.append(user_id)

async def disapprove(user_id: int):
    global pmap_data
    if user_id in pmap_data:
        pmap_data.remove(user_id)

async def is_approved(user_id: int):
    global pmap_data
    return user_id in pmap_data

async def list_approved():
    global pmap_data
    return pmap_data

async def add_warn(user_id: int):
    global warner_data
    warner_data[user_id] = warner_data.get(user_id, 0) + 1

async def reset_warns(user_id: int):
    global warner_data
    warner_data[user_id] = 0

async def get_warns(user_id: int):
    global warner_data
    return warner_data.get(user_id, 0)
