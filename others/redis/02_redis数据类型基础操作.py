import redis

pool = redis.ConnectionPool(host="127.0.0.1", port=6379, protocol=2)
r = redis.Redis(connection_pool=pool)

r.set("bar", "Foo")

# ===== 1. String 字符串 =====

# 增/改
r.set("name", "Tom")

# 查，默认返回 bytes
print("String get:", r.get("name"))

# 自增
r.incr("count")

# 自减
r.decr("count")

# 批量增/改
r.mset({"k1": "v1", "k2": "v2"})

# 批量查
print("String mget:", r.mget("k1", "k2"))

# 设置过期时间，单位秒
r.expire("name", 60)

# 查看剩余过期时间
print("String ttl:", r.ttl("name"))

# 删
r.delete("name")


# ===== 2. Hash 哈希 =====

# 增/改
r.hset("user:1", mapping={"name": "Tom", "age": 20})

# 查单个字段
print("Hash hget:", r.hget("user:1", "name"))

# 查多个字段
print("Hash hmget:", r.hmget("user:1", ["name", "age"]))

# 查全部字段
print("Hash hgetall:", r.hgetall("user:1"))

# age 字段加 1
r.hincrby("user:1", "age", 1)

# 删字段
r.hdel("user:1", "age")

# 判断字段是否存在
print("Hash hexists:", r.hexists("user:1", "age"))

# 删整个 key
r.delete("user:1")


# ===== 3. List 列表 =====

# 右边插入
r.rpush("list:1", "a", "b", "c")

# 左边插入
r.lpush("list:1", "z")

# 查全部
print("List lrange:", r.lrange("list:1", 0, -1))

# 左边弹出
print("List lpop:", r.lpop("list:1"))

# 右边弹出
print("List rpop:", r.rpop("list:1"))

# 长度
print("List llen:", r.llen("list:1"))

# 删除元素 b
r.lrem("list:1", 0, "b")

# 删整个 key
r.delete("list:1")


# ===== 4. Set 集合 =====

# 增
r.sadd("set:1", "a", "b", "c")

# 查全部成员
print("Set smembers:", r.smembers("set:1"))

# 判断成员是否存在
print("Set sismember:", r.sismember("set:1", "a"))

# 成员数量
print("Set scard:", r.scard("set:1"))

# 删成员
r.srem("set:1", "a")

# 增另一个集合
r.sadd("set:2", "b", "c", "d")

# 交集
print("Set sinter:", r.sinter("set:1", "set:2"))

# 并集
print("Set sunion:", r.sunion("set:1", "set:2"))

# 差集
print("Set sdiff:", r.sdiff("set:1", "set:2"))

# 删整个 key
r.delete("set:1", "set:2")


# ===== 5. ZSet 有序集合 =====

# 增/改
r.zadd("rank", {"tom": 100, "jerry": 90, "alice": 80})

# 按分数升序查
print("ZSet zrange:", r.zrange("rank", 0, -1, withscores=True))

# 按分数降序查
print("ZSet zrevrange:", r.zrevrange("rank", 0, -1, withscores=True))

# 查单个成员分数
print("ZSet zscore:", r.zscore("rank", "tom"))

# tom 分数加 5
r.zincrby("rank", 5, "tom")

# 查升序排名
print("ZSet zrank:", r.zrank("rank", "tom"))

# 查降序排名
print("ZSet zrevrank:", r.zrevrank("rank", "tom"))

# 成员数量
print("ZSet zcard:", r.zcard("rank"))

# 按分数范围查
print("ZSet zrangebyscore:", r.zrangebyscore("rank", 90, 100, withscores=True))

# 删成员
r.zrem("rank", "jerry")

# 删整个 key
r.delete("rank")